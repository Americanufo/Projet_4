from controllers.player_controller import PlayerController
from models.round import Round
from models.player import Player

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
        self.current_round_number = 1
    

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
        if not next_round:
            print("Aucun tour à lancer.")
            return
        print(f"Début du tour {self.current_round_number}...")
            
       
    # Tant qu'il y à des tournois il faut les lancer sachant que le nombre de tour est limité à 4
        while next_round:
            print(f"Lancement du tour {self.current_round_number}...")  
            next_round = self.next_round()
        print("Tous les tours ont été joués.")

    def next_round(self):
        if len (self.rounds) < self.nb_rounds:
            self.current_round_number += 1
            round_ = Round(self)
            self.rounds.append(round_)
            return round_
        else:
            print("Tournois terminé.")
            return None
    