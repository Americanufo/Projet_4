import os
from views.menu import display_main_menu
from controllers.reports_controller import reports
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from views.tournament_view import Terminal_view

# Vérifie si les dossiers nécessaires existent
if not os.path.exists("data/tournaments"):
    os.makedirs("data/tournaments")
 
Terminal_view.show_welcome()
# Demande à l'utilisateur de choisir une option
display_main_menu()
# Boucle principale du programme
while True:
    choice = input("Choisissez une option (1-5) : ")
    if choice == "1":
        Terminal_view.show_add_player()
        # Appeler la fonction pour ajouter un joueur
        player_controller = PlayerController()
        last_name = input("Nom de famille : (ex: Dupont)") or "Dupont"
        first_name = input("Prénom : (ex: Jean)") or "Jean"
        birth_date = input("Date de naissance (JJ/MM/AAAA) : (ex: 01/01/2000)") or "01/01/2000"
        chess_id = input("ID d'échecs : (ex: AB12345)") or "AB12345"
        player_controller.add_player(last_name, first_name, birth_date, chess_id)
        Terminal_view.show_player_added(first_name, last_name)
        display_main_menu()
    elif choice == "2":
        Terminal_view.show_create_tournament()
        display_main_menu()
        # Appeler la fonction pour créer un tournoi
        tournament_controller = TournamentController()
        name = input("Nom du tournoi : (ex: Tournoi de Paris)") or "Tournoi de Paris"
        location = input("Lieu du tournoi : (ex: Paris)") or "Paris"
        start_date = input("Date de début (JJ/MM/AAAA) : (ex: 01/04/2025)") or "01/04/2025"
        end_date = input("Date de fin (JJ/MM/AAAA) : (ex: 01/04/2025)") or "01/04/2025"
        description = input("Description du tournoi : (ex: Tournoi rapide) ") or "Tournoi rapide"
        rounds = input("Nombre de tours : (ex: 4)") or "4"
        playerController = PlayerController()
        Terminal_view.show_players(playerController.players)
        players_ids = input("ID des joueurs (séparés par des virgules) ") or "NOR00123, USA00245, FRA00345, CHN00467"
        ids = [id.strip() for id in players_ids.split(",")]
        # Créer le tournoi
        tournament = tournament_controller.add_tournament(name, location, start_date, end_date, description, int(rounds), ids)
        tournament.start()
        tournament_controller.save_to_json(tournament)
        Terminal_view.show_tournament_created(name)
        display_main_menu()
    elif choice == "3":
        #Terminal_view.
        # Appeler la fonction pour reprendre un tournois en cour
        #reports()
        display_main_menu()
    elif choice == "4":
        Terminal_view.show_reports()
        # Appeler la fonction pour voir les rapports
        reports()
        display_main_menu()
    elif choice == "5":
        Terminal_view.show_exit()
        # Quitter le programme   
        break
    else:
        Terminal_view.show_invalid_choice()
        display_main_menu()