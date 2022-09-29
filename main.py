import api.history as api
import data_base.postgres as db
import files.get_config as get_config

def main():
    print(get_config.api_key())

if __name__ == '__main__':
    main()