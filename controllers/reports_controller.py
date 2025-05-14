import json
from views.reports_views import Reports_view

def load_tournaments_from_json(path="data/tournaments/tournaments.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        Reports_view.show_no_tournaments()
        return []
    except json.JSONDecodeError:
        print("\nLe fichier de tournois est corrompu ou vide.\n")
        return []

def reports():
    tournaments = load_tournaments_from_json()
    if not tournaments:
        return

    while True:
        Reports_view.show_reports_menu()
        choice = input("Votre choix : ")
        if choice == "1":
            Reports_view.show_tournaments_list(tournaments)
            try:
                num = int(input("Sélectionnez le numéro du tournoi : "))
                if 1 <= num <= len(tournaments):
                    Reports_view.show_tournament_details(tournaments[num - 1])
                else:
                    Reports_view.show_invalid_number()
            except ValueError:
                Reports_view.show_invalid_entry()
        elif choice == "2":
            Reports_view.show_goodbye()
            break
        else:
            Reports_view.show_invalid_choice()
