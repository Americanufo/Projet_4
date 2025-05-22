import os
import json
from models.tournament import Tournament
from views.tournament_view import Terminal_view

class TournamentController:

    def __init__(self):
        self.tournaments = []

    def add_tournament(self, name, location, start_date, end_date, description="", rounds=4, players_ids=None):
        tournament = Tournament(name, location, start_date, end_date, description, rounds, players_ids)
        self.tournaments.append(tournament)
        return tournament

    def save_to_json(self, tournament):
        file_path = "data/tournaments/tournaments.json"
        tournaments_data = []

        # Lire les tournois existants s'il y en a
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                try:
                    tournaments_data = json.load(f)
                except json.JSONDecodeError:
                    tournaments_data = []

        # Supprimer les doublons (même nom + même date de début)
        tournaments_data = [
            t for t in tournaments_data
            if not (t["name"] == tournament.name and t["start_date"] == tournament.start_date)
        ]

        # Ajouter le tournoi mis à jour
        tournaments_data.append(tournament.to_dict())

        # Sauvegarder la liste complète
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(tournaments_data, f, ensure_ascii=False, indent=4)
