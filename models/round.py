from views.tournament_view import Terminal_view

class Round:
    def __init__(self, tournament):
        self.tournament = tournament
        Terminal_view.show_round(self.tournament)
        # On crée un match pour chaque pair de joueurs   
        self.matches = []
        for i in range(0, len(self.tournament.players) - 1, 2):
            self.matches.append(([self.tournament.players[i], None], [self.tournament.players[i + 1], None]))
        Terminal_view.show_matches(self.matches, with_scores=False)
        

    def saisir_scores(self):
        # Demande à l'utilisateur de saisir les scores pour chaque match
        for match in self.matches:
            player1, _ = match[0]
            player2, _ = match[1]
            while True:
                score1 = input(f"Score pour {player1.first_name} {player1.last_name} (0, 0.5, 1) : ")
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
            player1.score_tournament += score1
            player2.score_tournament += score2
        Terminal_view.show_scores_save()
        Terminal_view.show_matches(self.matches, with_scores=True)

    def to_dict(self):
        # On structure chaque match pour l'enregistrement des fichier JSON
        matches_list = []
        for match in self.matches:
            player1, score1 = match[0]
            player2, score2 = match[1]
            matches_list.append({
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
            })
        return {
            "matches": matches_list
        }
    

        
        
    