# Impression des tournois
class Terminal_view:
    def __init__(self):
        pass

    @staticmethod
    def show_round_start(round_number):
        print(f"Lancement du tour {round_number}...")

    @staticmethod
    def show_all_rounds_played():
        print("Tous les tours ont été joués.")

    @staticmethod
    def show_tournement_end():
        print("Tournois terminé.")

    @staticmethod
    def show_players(players):
        print("Liste des joueurs :")
        for player in players:
            print(player)

    @staticmethod
    def show_no_players():
        print("Aucun joueur dans le tournoi.")

    @staticmethod
    def show_winner(winner, score):
        print(f"Le vainqueur est : {winner} avec {score} points.")

    @staticmethod
    def show_equality():
        print("Il y a une égalité entre :")

    @staticmethod
    def show_equality_player(player):
        print(f"- {player.first_name} {player.last_name} ({player.score_tournament} points)") 