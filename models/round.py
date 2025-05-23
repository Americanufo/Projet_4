import random
from views.tournament_view import Terminal_view


class Round:
    def __init__(self, tournament):
        self.tournament = tournament
        Terminal_view.show_round(self.tournament)
        self.matches = []

        # Génération des paires pour le tour
        if tournament.current_round_number == 1:
            # Premier tour : mélange aléatoire des joueurs
            players = self.tournament.players[:]
            random.shuffle(players)
        else:
            # Tours suivants : tri des joueurs par score, puis mélange des ex-aequo
            players = sorted(self.tournament.players,
                             key=lambda p: p.score_tournament, reverse=True)
            # Mélange les groupes d'ex-aequo pour varier les appariements
            i = 0
            while i < len(players):
                score = players[i].score_tournament
                j = i + 1
                while j < len(
                        players) and players[j].score_tournament == score:
                    j += 1
                random.shuffle(players[i:j])
                i = j

        # On crée un match pour chaque pair de joueurs en évitant les re-matches
        available_players = players[:]
        while len(available_players) >= 2:
            player1 = available_players.pop(0)
            # Cherche un adversaire que le joueur n'a pas encore rencontré
            for idx, player2 in enumerate(available_players):
                if player2.chess_id not in player1.opponents:
                    self.matches.append(([player1, None], [player2, None]))
                    # On mémorise que ces deux joueurs se sont rencontrés
                    player1.opponents.append(player2.chess_id)
                    player2.opponents.append(player1.chess_id)
                    available_players.pop(idx)
                    break
            else:
                # Si tous les autres ont déjà été rencontrés, on prend le suivant
                player2 = available_players.pop(0)
                self.matches.append(([player1, None], [player2, None]))
                player1.opponents.append(player2.chess_id)
                player2.opponents.append(player1.chess_id)

        # Affiche les matchs du round (scores non renseignés)
        Terminal_view.show_matches(self.matches, with_scores=False)

    def from_dict(self, round_dict):

        # Recharge les matches et scores depuis un dictionnaire (pour la reprise d'un tournoi).

        self.matches = []
        matches = round_dict.get("matches", {})
        # Parcours les matchs dans l'ordre des clés (match_1, match_2, ...)
        for match_num in sorted(
            matches.keys(), key=lambda x: int(
                x.split("_")[1])):
            match = matches[match_num]
            # Recherche les objets Player à partir de leur chess_id
            player1 = next((p for p in self.tournament.players if p.chess_id ==
                           match["player1"]["chess_id"]), None)
            player2 = next((p for p in self.tournament.players if p.chess_id ==
                           match["player2"]["chess_id"]), None)
            score1 = match.get("score1")
            score2 = match.get("score2")
            self.matches.append(([player1, score1], [player2, score2]))
            # Mise à jour des scores dans le tournoi
            if score1 is not None:
                player1.score_tournament += score1
            if score2 is not None:
                player2.score_tournament += score2

    def saisir_scores(self):
        # Demande à l'utilisateur de saisir les scores pour chaque match
        for match in self.matches:
            player1, _ = match[0]
            player2, _ = match[1]
            while True:
                score1 = input(f"Score pour {player1.first_name} {
                               player1.last_name} (0, 0.5, 1) : ")
                if score1 in ["0", "0.5", "1"]:
                    score1 = float(score1)
                    break
                else:
                    Terminal_view.show_please_input()
            # Calcul du score du second joueur
            if score1 == 0:
                score2 = 1
            elif score1 == 0.5:
                score2 = 0.5
            else:
                score2 = 0

            # Correction pour un affichage propre dans le fichier JSON
            if score1.is_integer():
                score1 = int(score1)
            if isinstance(score2, float) and score2.is_integer():
                score2 = int(score2)

            match[0][1] = score1
            match[1][1] = score2
            # Mise à jour des scores dans le tournoi
            player1.score_tournament += score1
            player2.score_tournament += score2

        Terminal_view.show_scores_save()
        # Affiche les matchs du round avec les scores renseignés
        Terminal_view.show_matches(self.matches, with_scores=True)

    def to_dict(self):
        # On structure chaque match pour l'enregistrement des fichiers JSON
        matches_dict = {}
        for i, match in enumerate(self.matches, start=1):
            player1, score1 = match[0]
            player2, score2 = match[1]
            matches_dict[f"match_{i}"] = {
                "player1": {
                    "first_name": player1.first_name,
                    "last_name": player1.last_name,
                    "chess_id": player1.chess_id
                },
                "score1": score1,
                "player2": {
                    "first_name": player2.first_name,
                    "last_name": player2.last_name,
                    "chess_id": player2.chess_id
                },
                "score2": score2
            }
        return {
            "matches": matches_dict
        }
