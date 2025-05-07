
import json
# On charge le fichier JSON Tournaments
def load_tournaments_from_json(path="data/tournaments/tournaments.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Aucun fichier de tournois trouvé.")
        return []
    except json.JSONDecodeError:
        print("Le fichier de tournois est corrompu ou vide.")
        return []

# Affichage des détails du tournoi
def display_tournament_details(tournament):
    print(f"\n=== Détails du tournoi : {tournament['name']} ===")
    print(f"Lieu : {tournament['location']}")
    print(f"Dates : {tournament['start_date']} au {tournament['end_date']}")
    print(f"Description : {tournament['description']}\n")

    players = sorted(
        tournament.get("players", []),
        key=lambda x: (x["last_name"].upper(), x["first_name"].upper())
    )
    print("Joueurs du tournoi (ordre alphabétique) :")
    for player in players:
        print(f"- {player['first_name']} {player['last_name']} (ID : {player['chess_id']})")

    print("\nTours et matchs :")
    for i, round_ in enumerate(tournament.get("rounds", []), 1):
        print(f"\nTour {i} :")
        for match in round_["matches"]:
            p1 = match["player1"]
            p2 = match["player2"]
            print(f"  {p1['first_name']} {p1['last_name']} ({match['score1']})"
                  f" vs {p2['first_name']} {p2['last_name']} ({match['score2']})")

# Menu des rapports
def reports():
    tournaments = load_tournaments_from_json()
    if not tournaments:
        print("Aucun tournoi à afficher.")
        return

    while True:
        print("\n=== Menu des rapports ===")
        print("1. Afficher les résultats d'un tournoi")
        print("2. Quitter")
        choice = input("Votre choix : ")
        if choice == "1":
            print("\nListe des tournois :")
            for idx, tournament in enumerate(tournaments, 1):
                print(f"{idx}. {tournament['name']} ({tournament['start_date']} au {tournament['end_date']})")
            try:
                num = int(input("Sélectionnez le numéro du tournoi : "))
                if 1 <= num <= len(tournaments):
                    display_tournament_details(tournaments[num - 1])
                else:
                    print("Numéro invalide.")
            except ValueError:
                print("Entrée invalide.")
        elif choice == "2":
            print("Merci, à bientôt !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")