from models.player import Player

class PlayerController:
    def __init__(self):
        self.players = [
    Player(last_name="Carlsen", first_name="Magnus", birth_date="1990-11-30", chess_id="NOR00123"),
    Player(last_name="Niemann", first_name="Hans", birth_date="2003-06-20", chess_id="USA00245"),
    Player(last_name="Firouzja", first_name="Alireza", birth_date="2003-06-18", chess_id="FRA00345"),
    Player(last_name="Ding", first_name="Liren", birth_date="1992-10-24", chess_id="CHN00467"),
    Player(last_name="Nepomniachtchi", first_name="Ian", birth_date="1990-07-14", chess_id="RUS00556")
]

    def add_player(self, last_name, first_name, birth_date, chess_id):
        player = Player(last_name, first_name, birth_date, chess_id)
        self.players.append(player)