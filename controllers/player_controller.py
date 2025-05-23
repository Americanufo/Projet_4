import os
import json
from models.player import Player


class PlayerController:
    def __init__(self):
        self.players = []
        self.load_from_json()

    def load_from_json(self):
        file_path = "data/tournaments/players.json"
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                try:
                    players_data = json.load(f)
                    self.players = [Player(**data) for data in players_data]
                except json.JSONDecodeError:
                    self.players = []
        else:
            self.players = []

    def add_player(self, last_name, first_name, birth_date, chess_id):
        player = Player(last_name, first_name, birth_date, chess_id)
        self.players.append(player)
        self.save_to_json(player)

    def save_to_json(self, player):
        file_path = "data/tournaments/players.json"
        player_data = []

    # Lire les joueurs existants s'il y en a
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                try:
                    player_data = json.load(f)
                except json.JSONDecodeError:
                    player_data = []
    # Ajouter les nouveaux joueurs
        player_data.append(player.to_dict())

        # Sauvegarder la liste complète
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(player_data, f, ensure_ascii=False, indent=4)
