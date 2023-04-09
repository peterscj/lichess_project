import berserk
import chess
import chess.pgn
from datetime import datetime

id = 'peterscj'

class GetLichessData:
    def __init__(self, token):
        # Establish Connection
        self.token = token
        self.establish_connection()
        self.get_game_data()

    def establish_connection(self):
        session = berserk.TokenSession(self.token)
        self.client = berserk.Client(session=session)
        print("Establishing connection...")

    def get_game_data(self):
        start = berserk.utils.to_millis(datetime(2022, 12, 8))
        end = berserk.utils.to_millis(datetime(2023, 2, 9))
        gen = self.client.games.export_by_player(id, since=start, until=end,max=300)

        # Put data in list so that we may view it
        games = list(gen)

        with open("pgn_output.txt", "w", encoding='utf8') as f:
            final_pgn = str()
            for index, game in enumerate(games):
                    game_id = games[index]['id']
                    pgn = self.client.games.export(game_id, as_pgn=True)
                    final_pgn += pgn
                    print(f'I wrote {index+1} games to file...')
            f.write(final_pgn)