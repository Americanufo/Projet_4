from controllers.player_controller import PlayerController
from models.round import Round
from models.player import Player
import json
import re

class Tournament:
    def __init__(self, name, location, start_date, end_date, description="", nb_rounds=4, players_ids=None):
        self.nb_rounds = nb_rounds
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.rounds = []
        self.players = [player for player in PlayerController().players if player.chess_id in players_ids] if players_ids else []
        for player in self.players:
            player.score_tournament = 0
        self.current_round_number = 0

    

    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "rounds": [round_.to_dict() for round_ in self.rounds],
            "players": [player.to_dict() for player in self.players],
            "current_round_number": self.current_round_number,
        }
    
    def start(self):
        print(f"Début du tournoi {self.name} à {self.location} du {self.start_date} au {self.end_date}.")
        print(f"Description: {self.description}")
        print(f"Nombre de tours: {self.nb_rounds}")
        print(f"Début du tournoi avec {len(self.players)} joueurs.")
        

    #    On lance le premier tour
        next_round = self.next_round()

            
       
    # Tant qu'il y à des tournois il faut les lancer sachant que le nombre de tour est limité à 4
        while next_round:
            print(f"Lancement du tour {self.current_round_number}...")  
            next_round.saisir_scores()
            next_round = self.next_round()
        print("Tous les tours ont été joués.")
        self.get_winner()
        self.save_to_json()

    def next_round(self):
        if len (self.rounds) < self.nb_rounds:
            self.current_round_number += 1
            round_ = Round(self)
            self.rounds.append(round_)
            return round_
        else:
            print("Tournois terminé.")
            print(self.players)
            return None
    
    def get_winner(self):
        if not self.players:
            print("Aucun joueur dans le tournoi.")
            return None
    # Trouver le score maximal
        max_score = max(player.score_tournament for player in self.players)
    # Trouver les joueurs ayant le score maximal
        winners = [player for player in self.players if player.score_tournament == max_score]

        if len(winners) == 1:
            print(f"Le vainqueur est : {winners[0].first_name} {winners[0].last_name} avec {max_score} points.")
            return winners[0]
        else:
            print("Il y a une égalité entre :")
            for player in winners:
                print(f"- {player.first_name} {player.last_name} ({player.score_tournament} points)")
            return winners
        
    def save_to_json(self):
        # Nettoyer le nom du tournoi et la date
        safe_name = re.sub(r'[^a-zA-Z0-9_-]', '_', self.name.strip()).lower()
        safe_date = re.sub(r'[^0-9]', '', self.start_date)
        file_name = f"{safe_name}_{safe_date}.json"
        file_path = f"data/tournaments/{file_name}"

        # Sauvegarder au format JSON
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=4)
        print(f"Tournoi sauvegardé dans {file_path}")    
