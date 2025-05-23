from controllers.player_controller import PlayerController
from models.round import Round
from views.tournament_view import Terminal_view


class Tournament:
    def __init__(
            self,
            name,
            location,
            start_date,
            end_date,
            description="",
            nb_rounds=4,
            players_ids=None):
        self.nb_rounds = nb_rounds
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.rounds = []
        self.players = [player for player in PlayerController(
        ).players if player.chess_id in players_ids] if players_ids else []
        for player in self.players:
            player.score_tournament = 0
            player.opponents = []
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
        Terminal_view.show_start(self)
        from controllers.tournament_controller import TournamentController
        tournament_controller = TournamentController()

        # Tant qu'il reste des tours à jouer (limité par nb_rounds)
        while len(self.rounds) < self.nb_rounds:
            next_round = self.next_round()
            if not next_round:
                break
            Terminal_view.show_round_start(self.current_round_number)
            next_round.saisir_scores()
            tournament_controller.save_to_json(self)
            # Proposer de continuer ou sortir
            choix = input(
                "Voulez-vous continuer le tournoi ? (o/n) : ").lower()
            if choix != "o":
                print("Tournoi sauvegardé. Retour au menu principal.")
                return

        # Fin du tournoi
        Terminal_view.show_all_rounds_played()
        self.get_winner()
        tournament_controller.save_to_json(self)

    def next_round(self):
        # Si le nombre de rounds n'est pas atteint, on crée un nouveau round
        if len(self.rounds) < self.nb_rounds:
            self.current_round_number = len(self.rounds) + 1
            round_ = Round(self)
            self.rounds.append(round_)
            return round_
        else:
            # Si tous les rounds sont joués, on affiche la fin du tournoi
            Terminal_view.show_tournement_end()
            Terminal_view.show_players_final(self.players)
            return None

    def get_winner(self):
        if not self.players:
            Terminal_view.show_no_players()
            return None
        # Trouver le score maximal
        max_score = max(player.score_tournament for player in self.players)
        # Trouver les joueurs ayant le score maximal
        winners = [
            player for player in self.players if player.score_tournament == max_score]
        # Stocker les scores de chaque joueur pour le JSON
        self.player_points = {f"{player.first_name} {
            player.last_name}": player.score_tournament for player in self.players}

        if len(winners) == 1:
            winner_name = [f"{winners[0].first_name} {winners[0].last_name}"]
            Terminal_view.show_winner(winner_name, max_score)
            self.winner = winner_name
            return winners[0]
        else:
            Terminal_view.show_equality()
            winner_names = []
            for player in winners:
                name = f"{player.first_name} {player.last_name}"
                Terminal_view.show_equality_player(player)
                winner_names.append(name)
            self.winner = winner_names
            return winners
