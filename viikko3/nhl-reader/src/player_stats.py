from datetime import datetime

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        all_players = self.reader.get_players()
        players_of_country = []
        for player in all_players:
            if player.nationality == nationality:
                players_of_country.append(player)
        players_of_country.sort(key=lambda players: players.goals + players.assists, reverse=True)
        print(f"Players from {nationality}", datetime.now(), "\n")
        return players_of_country
