class Round:
    def __init__(self, tournament):
        self.tournament = tournament
        print(f"Début du tour {tournament.current_round_number}...")
        # On crée un match pour chaque pair de joueurs   
        self.matches = []
        for i in range(0, len(self.tournament.players) - 1, 2):
            self.matches.append(([self.tournament.players[i], None], [self.tournament.players[i + 1], None]))
        print(self.matches)

        # Demande à l'utilisateur de saisir les scores pour chaque match
        for match in self.matches:
            player1, player2 = match
            score1 = input(f"Score pour {player1[0].first_name} {player1[0].last_name} (0, 0.5, 1) : ")
            match[0][1] = float(score1)
            if score1 == "0":
                score2 = "1"
            elif score1 == "0.5":
                score2 = "0.5"
            else:
                score2 = "0"
            match[1][1] = float(score2)
            match[0][0].score_tournament += float(score1)
            match[1][0].score_tournament += float(score2)
        print("Scores enregistrés !")
      
        

        
        
    