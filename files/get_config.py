from pathlib import Path
import yaml
from yaml.loader import SafeLoader

def read_config(file: str):
    path = Path(__file__).parents[1]
    path = path.joinpath('config', file + '.yaml')
    with path.open() as f:
        data = yaml.load(f, Loader = SafeLoader)
    f.close()

    return data

def api_key():
    data = read_config('passwords')
    return data['api_key']

def db_data():
    data = read_config('passwords')
    return {'user' : data['db_user'], 'password' : data['db_password']}

def start_time():
    data = read_config('config')
    return data['start_time']