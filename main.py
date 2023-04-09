# import requests
# import berserk
# import chess
# import chess.pgn
# import pandas as pd
from converter.pgn_data import PGNData
from api_connector import GetLichessData

pgn_file = "pgn_output.txt"
api_file = "C:/Users/cole/Documents/lichess_api_token.txt"

def extract_chess_data(pgn_file,token):
    try:
        with open(pgn_file) as f:
            raw_pgn = f.read()
            if len(raw_pgn) == 0: GetLichessData(token)

    except FileNotFoundError:
        GetLichessData(token)
        with open(pgn_file) as f:
            raw_pgn = f.read()

    return raw_pgn

# Get api token saved locally
with open(f"{api_file}") as f:
    api_token = f.read()

# Fetch pgn data from lichess api and export to tabular format
raw_pgn_file = extract_chess_data(pgn_file, api_token)
pgn_data = PGNData(pgn_file)
pgn_data.export()