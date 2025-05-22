class ResumeTournamentView:
    @staticmethod
    def show_tournaments_list(tournaments):
        print("\nListe des tournois en cours :")
        for idx, tournament in enumerate(tournaments, 1):
            print(f"{idx}. {tournament['name']} ({tournament['start_date']} au {tournament['end_date']})")
        print()

    @staticmethod
    def show_no_tournaments():
        print("\nAucun tournoi en cours à reprendre.\n")

    @staticmethod
    def show_invalid_number():
        print("\nNuméro invalide.\n")

    @staticmethod
    def show_invalid_entry():
        print("\nEntrée invalide.\n")
