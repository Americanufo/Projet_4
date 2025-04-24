from models.tournament import Tournament

class TournamentController:
    def __init__(self):
        self.tournaments = []

    def add_tournament(self, name, location, start_date, end_date, description="", rounds=4, players_ids=None):
        tournament = Tournament(name, location, start_date, end_date, description, rounds, players_ids)
        self.tournaments.append(tournament)
        return tournament