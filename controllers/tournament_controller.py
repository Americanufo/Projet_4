from models.tournament import Tournament
import json 
import re

class TournamentController:
    def __init__(self):
        self.tournaments = []
        
    def add_tournament(self, name, location, start_date, end_date, description="", rounds=4, players_ids=None):
        tournament = Tournament(name, location, start_date, end_date, description, rounds, players_ids)
        self.tournaments.append(tournament)
        return tournament
    

    def save_to_json(self, tournament):
        # Nettoyer le nom du tournoi et la date
        safe_name = re.sub(r'[^a-zA-Z0-9_-]', '_', tournament.name.strip()).lower()
        safe_date = re.sub(r'[^0-9]', '', tournament.start_date)
        file_name = f"{safe_name}_{safe_date}.json"
        file_path = f"data/tournaments/{file_name}"


        # Sauvegarder au format JSON
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(tournament.to_dict(), f, ensure_ascii=False, indent=4)
        print(f"Tournoi sauvegardé dans {file_path}")    