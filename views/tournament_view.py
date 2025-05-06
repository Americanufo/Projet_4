# Impression des tournois
def show_round_start(round_number):
    print(f"Lancement du tour {round_number}...")

def show_all_rounds_played():
    print("Tous les tours ont été joués.")

def show_tournement_end():
    print("Tournois terminé.")

def show_players(players):
    print("Liste des joueurs :")
    for player in players:
        print(player)

def show_no_players():
    print("Aucun joueur dans le tournoi.")

def show_winner(winner, score):
    print(f"Le vainqueur est : {winner} avec {score} points.")

def show_equality():
    print("Il y a une égalité entre :")

def show_equality_player(player):
    print(f"- {player.first_name} {player.last_name} ({player.score_tournament} points)") 