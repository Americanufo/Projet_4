# Impression des tournois
class Terminal_view:
    def __init__(self):
        pass

    @staticmethod
    def show_round_start(round_number):
        print(f"\nLancement du tour {round_number}...\n")

    @staticmethod
    def show_all_rounds_played():
        print("\nTous les tours ont été joués.\n")

    @staticmethod
    def show_tournement_end():
        print("\nTournois terminé.\n")

    @staticmethod
    def show_players(players):
        print("\nListe des joueurs inscrits :\n")
        print('{:<15} {:<15} {:<15} {:<12}'.format('Prénom', 'Nom', 'Date de naissance', "ID d'échecs"))
        print("-" * 60)
        for player in players:
            print('{:<15} {:<15} {:<15} {:<12}'.format(
                player.first_name, player.last_name, player.birth_date, player.chess_id
            ))
        print()
    
    @staticmethod
    def show_matches(matches, with_scores=False):
        print("\nMatchs du round :")
        for match in matches:
            (player1, score1), (player2, score2) = match
            if with_scores:
             s1 = "" if score1 is None else score1
             s2 = "" if score2 is None else score2
             print(f"  {player1.first_name} {player1.last_name} ({s1}) vs {player2.first_name} {player2.last_name} ({s2})")
            else:
             print(f"  {player1.first_name} {player1.last_name} vs {player2.first_name} {player2.last_name}")
    print()

    @staticmethod
    def show_no_players():
        print("\nAucun joueur dans le tournoi.\n")

    @staticmethod
    def show_winner(winner, score):
        print(f"\nLe vainqueur est : {winner} avec {score} points.\n")

    @staticmethod
    def show_equality():
        print("\nIl y a une égalité entre :\n")

    @staticmethod
    def show_equality_player(player):
        print(f"- {player.first_name} {player.last_name} ({player.score_tournament} points)")

    @staticmethod
    def show_start(self):
        print(f"\nDébut du tournoi {self.name} à {self.location} du {self.start_date} au {self.end_date}.")
        print(f"Description: {self.description}")
        print(f"Nombre de tours: {self.nb_rounds}")
        print(f"Début du tournoi avec {len(self.players)} joueurs.\n")

    @staticmethod
    def show_round(tournament):
        print(f"\nDébut du tour {tournament.current_round_number}...\n")

    @staticmethod
    def show_please_input():
        print("\nVeuillez entrer 0, 0.5 ou 1.\n")

    @staticmethod
    def show_scores_save():
        print("\nScores enregistrés !\n")

    @staticmethod
    def show_welcome():
        print("\nBienvenu dans Chess Manager\n")

    @staticmethod
    def show_add_player():
        print("\nAjouter un joueur\n")

    @staticmethod
    def show_player_added(first_name, last_name):
        print(f"\nJoueur {first_name} {last_name} ajouté avec succès !\n")

    @staticmethod
    def show_create_tournament():
        print("\nCréer un tournoi\n")

    @staticmethod
    def show_tournament_created(name):
        print(f"\n{name} créé avec succès !\n")

    @staticmethod
    def show_reports():
        print("\nVoir les rapports\n")

    @staticmethod
    def show_exit():
        print("\nMerci d'avoir utilisé Chess Manager ! Au revoir !\n")

    @staticmethod
    def show_invalid_choice():
        print("\nChoix invalide. Veuillez choisir une option valide.\n")

    @staticmethod
    def show_tournament_saved(file_path):
        print(f"\nTournoi sauvegardé dans {file_path}\n")

    @staticmethod
    def show_players_saved(file_path):
        print(f"\nJoueurs sauvegardés dans {file_path}\n")
