import json
from models.tournament import Tournament
from models.round import Round
from views.resume_tournament_view import ResumeTournamentView
from controllers.tournament_controller import TournamentController

def load_tournaments_from_json(path="data/tournaments/tournaments.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def resume_tournament():
    tournaments = load_tournaments_from_json()
    # Filtrer les tournois non terminés (on utilise la longueur de rounds pour être sûr)
    tournaments_in_progress = [t for t in tournaments if len(t.get("rounds", [])) < t.get("nb_rounds", 4)]
    if not tournaments_in_progress:
        ResumeTournamentView.show_no_tournaments()
        return

    ResumeTournamentView.show_tournaments_list(tournaments_in_progress)
    try:
        num = int(input("Sélectionnez le numéro du tournoi à reprendre : "))
        if 1 <= num <= len(tournaments_in_progress):
            t = tournaments_in_progress[num - 1]
            # Recréer l'objet Tournament
            tournament = Tournament(
                name=t['name'],
                location=t['location'],
                start_date=t['start_date'],
                end_date=t['end_date'],
                description=t.get('description', ""),
                nb_rounds=t.get('nb_rounds', 4),
                players_ids=[p['chess_id'] for p in t['players']]
            )
            # Recharger les rounds déjà joués 
            tournament.rounds = []
            if "rounds" in t:
                for round_dict in t["rounds"]:
                    round_obj = Round(tournament)
                    round_obj.from_dict(round_dict)
                    tournament.rounds.append(round_obj)
            # Met à jour le numéro du round courant pour la reprise
            tournament.current_round_number = len(tournament.rounds)

            tournament.start()
            TournamentController().save_to_json(tournament)
        else:
            ResumeTournamentView.show_invalid_number()
    except ValueError:
        ResumeTournamentView.show_invalid_entry()
