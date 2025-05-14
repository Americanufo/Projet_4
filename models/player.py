class Player:
    def __init__(self, last_name, first_name, birth_date, chess_id, points=0, score_tournament=0):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.chess_id = chess_id
        self.points = points
        self.score_tournament = score_tournament
        self.opponents = [] # Liste des adversaires déjà rencontrés

    def to_dict(self):
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "chess_id": self.chess_id,
            "score_tournament": self.score_tournament
        }
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.chess_id})"
    def __repr__(self):
        return f"Player({self.first_name}, {self.last_name}, {self.birth_date}, {self.chess_id})"
