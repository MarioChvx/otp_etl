from pathlib import Path
import yaml
import json
from yaml.loader import SafeLoader

_path = Path(__file__).parents[1]
_path = _path.joinpath('config')

def read_config(file_name: str):
    type = file_name.split('.')[-1]

    with _path.joinpath(file_name).open('r') as f:
        if type == 'yaml':
            data = yaml.load(f, Loader = SafeLoader)
        elif type == 'json':
            data = json.load(f)
    f.close()

    return data

def write_players(players: dict):
    with _path.joinpath('players.json').open('w') as f:
        json.dump(players, f)
    f.close()


def api_key():
    data = read_config('passwords.yaml')
    return data['api_key']

def db_data():
    data = read_config('passwords.yaml')
    return {'user' : data['db_user'], 'password' : data['db_password'], 'name' : data['db_name']}

def start_time():
    data = read_config('config.yaml')
    return data['start_time']

def players_data():
    data = read_config('players.json')
    return data