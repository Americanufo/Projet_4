# Impression des rapports

class Reports_view:
    def __init__(self):
        pass

    @staticmethod
    def show_reports_menu():
        print("\n=== Menu des rapports ===")
        print("1. Afficher les résultats d'un tournoi")
        print("2. Quitter\n")

    @staticmethod
    def show_no_tournaments():
        print("\nAucun tournoi à afficher.\n")

    @staticmethod
    def show_tournaments_list(tournaments):
        print("\nListe des tournois :")
        for idx, tournament in enumerate(tournaments, 1):
            print(f"{idx}. {tournament['name']} ({tournament['start_date']} au {tournament['end_date']})")
        print()

    @staticmethod
    def show_invalid_number():
        print("\nNuméro invalide.\n")

    @staticmethod
    def show_invalid_entry():
        print("\nEntrée invalide.\n")

    @staticmethod
    def show_invalid_choice():
        print("\nChoix invalide, veuillez réessayer.\n")

    @staticmethod
    def show_goodbye():
        print("\nMerci, à bientôt !\n")

    @staticmethod
    def show_tournament_details(tournament):
        print(f"\n=== Détails du tournoi : {tournament['name']} ===")
        print(f"Lieu : {tournament['location']}")
        print(f"Dates : {tournament['start_date']} au {tournament['end_date']}")
        print(f"Description : {tournament['description']}\n")

        # Affichage des joueurs par ordre alphabétique
        players = sorted(
            tournament.get("players", []),
            key=lambda x: (x["last_name"].upper(), x["first_name"].upper())
        )
        print("Joueurs du tournoi (ordre alphabétique) :")
        for player in players:
            print(f"- {player['first_name']} {player['last_name']} (ID : {player['chess_id']})")

        # Classement final par score
        print("\nClassement final par score :")
        print('{:<15} {:<15} {:<15} {:<12} {:<6}'.format('Prénom', 'Nom', 'Date de naissance', "ID d'échecs", "Score"))
        print("-" * 75)
        players_sorted = sorted(
            tournament.get("players", []),
            key=lambda x: x.get("score_tournament", 0),
            reverse=True
        )
        for player in players_sorted:
            print('{:<15} {:<15} {:<15} {:<12} {:<6}'.format(
                player['first_name'],
                player['last_name'],
                player['birth_date'],
                player['chess_id'],
                player.get("score_tournament", 0)
            ))
        print()

        # Affichage des tours et des matchs
        print("\nTours et matchs :")
        for i, round_ in enumerate(tournament.get("rounds", []), 1):
            print(f"\nTour {i} :")
            matches = round_.get("matches", {})
            if matches:
                for match_num in sorted(matches.keys(), key=lambda x: int(x.split("_")[1])):
                    match = matches[match_num]
                    p1 = match["player1"]
                    p2 = match["player2"]
                    print(f" {p1['first_name']} {p1['last_name']} ({match['score1']})"
                          f" vs {p2['first_name']} {p2['last_name']} ({match['score2']})")
            else:
                print(" Aucun match enregistré pour ce tour.")

        # Affichage du vainqueur ou des ex aequo
        players = tournament.get("players", [])
        if players:
            max_score = max(p.get("score_tournament", 0) for p in players)
            winners = [p for p in players if p.get("score_tournament", 0) == max_score]
            if len(winners) == 1:
                w = winners[0]
                print(f"\nVainqueur du tournoi : {w['first_name']} {w['last_name']} ({w['score_tournament']} points)")
            else:
                print("\nVainqueurs ex aequo :")
                for w in winners:
                    print(f"- {w['first_name']} {w['last_name']} ({w['score_tournament']} points)")
        print()
