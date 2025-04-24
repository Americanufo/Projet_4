class Round:
    def __init__(self, tournament):
        self.tournament = tournament
        # On crée un match pour chaque pair de joueurs   
        self.matches = []
        for i in range(0, len(self.tournament.players) - 1, 2):
            self.matches.append(([self.tournament.players[i]], [self.tournament.players[i + 1]]))
        print(self.matches)

        # Demande à l'utilisateur de saisir les scores pour chaque match
        self.scores = {}
        for match in self.matches:
            player1, player2 = match
            score1 = input(f"Score pour {player1[0].first_name} {player1[0].last_name} (0, 0.5, 1) : ")
            score2 = input(f"Score pour {player2[0].first_name} {player2[0].last_name} (0, 0.5, 1) : ")
            self.scores[(player1[0], player2[0])] = (float(score1), float(score2))
            # Met à jour les points des joueurs
            player1[0].points += float(score1)
            player2[0].points += float(score2)
        print("Scores enregistrés !")
        print(self.scores)
        

        
        
    