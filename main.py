import api.history as api
import data_base.postgres as db
import files.get_config as get_config

def test():
    print('START') 
    _watcher = api.build_watcher()
    _start_epoch = get_config.start_time()
    _players = get_config.players_data()
    for player in _players:
        if player['puuid'] == '':
            player['puuid'] = api.get_player_puuid(player, _watcher)
        print(player)
    print(_players)

def main():
    test()

if __name__ == '__main__':
    main()