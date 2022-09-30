import api.history as api
import data_base.postgres as db
import files.get_config as config
import time

def test():
    print('START') 
    _watcher = api.build_watcher()
    _start_epoch = config.start_time()
    _players = config.players_data()

    # Validate players data and saving it
    for player in _players:
        if player['puuid'] == '':
            player['puuid'] = api.get_player_puuid(player, _watcher)
    config.write_players(_players)

    # Getting match_id's from the specified time
    _match_ids = ()
    while len(_match_ids) == 0:
        print(_start_epoch)
        _match_ids = api.players_matches_day(_players, _start_epoch, _watcher)
        _start_epoch += 86400
        time.sleep(5)

    # Getting details from matches
    _matches_details = []
    for match in _match_ids:
        match_details = api.match_details_by_region_and_id(match, _watcher)
        _matches_details.append(match_details)
        time.sleep(1)

    # print(_matches_details[0]['info'])

    # Build DataFrames
    df_pariticipations = api.df_participants_rows(_matches_details[0])
    print(df_pariticipations)

    for i in df_pariticipations:
        print(i)

    df_matches = api.df_match_row(_matches_details[0])
    print(df_matches)

    _connection = db.connection_history()
    _cursor = db.create_cursor(_connection)

    db.create_rows(df_matches, 'match', _cursor, _connection)
    db.create_rows(df_pariticipations, 'participation', _cursor, _connection)

def main():
    test()

if __name__ == '__main__':
    main()