from controllers.player_controller import PlayerController
from models.round import Round
from views.tournament_view import show_round_start, show_all_rounds_played, show_tournement_end, show_players, show_no_players, show_winner, show_equality, show_equality_player

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
        self.player_points = {}
        self.winner = None

    

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
            "player_points": self.player_points,
            "winner": self.winner
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
            show_round_start(self.current_round_number) 
            next_round.saisir_scores()
            next_round = self.next_round()
        show_all_rounds_played()
        self.get_winner()
        

    def next_round(self):
        if len (self.rounds) < self.nb_rounds:
            self.current_round_number += 1
            round_ = Round(self)
            self.rounds.append(round_)
            return round_
        else:
            show_tournement_end()
            show_players(self.players)
            return None
    
    def get_winner(self):
        if not self.players:
            show_no_players()
            return None
    # Trouver le score maximal
        max_score = max(player.score_tournament for player in self.players)
    # Trouver les joueurs ayant le score maximal
        winners = [player for player in self.players if player.score_tournament == max_score]
    # Stocker les scores de chaque joueur (pour le JSON)
        self.player_points = {f"{player.first_name} {player.last_name}": player.score_tournament for player in self.players}

        if len(winners) == 1:
            winner_name = f"{winners[0].first_name} {winners[0].last_name}"
            show_winner(winner_name, max_score)
            self.winner = winner_name
            return winners[0]
        else:
            show_equality()
            winner_names = []
            for player in winners:
                name = f"{player.first_name} {player.last_name}"
                show_equality_player(player)
                winner_names.append(name)
                self.winner = winner_names  
            return winners
        
    
