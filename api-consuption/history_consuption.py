from riotwatcher import LolWatcher, ApiError
import pandas as pd
from pathlib import Path

def read_api_key():
    path = Path(__file__).parent
    path = path.joinpath('apikey.txt')
    with path.open() as f:
        key = f.readline()
    f.close()
    return key
