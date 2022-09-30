from riotwatcher import LolWatcher, ApiError
import pandas as pd
import files.get_config as get_config
import numpy as np

def build_watcher():
    return LolWatcher(get_config.api_key())

def get_player_puuid(summoner, watcher):
    summoner_data = watcher.summoner.by_name(summoner['region'], summoner['name'])
    return summoner_data['puuid']

def players_matches_day(summoners, start_epoch, watcher):
    player_matches = []
    for summoner in summoners:
        matches_player = watcher.match.matchlist_by_puuid(summoner['region'], summoner['puuid'], start_time = start_epoch, end_time = start_epoch + 86400)
        player_matches += [(summoner['region'], match) for match in matches_player]
    return player_matches

def match_details_by_region_and_id(match, watcher):
    match_details = watcher.match.by_id(match[0], match[1])
    return match_details

def df_match_row(match):
    row_match = {
        'matchId' : [match['metadata']['matchId']],
        'gameCreation' : [match['info']['gameCreation']],
        'gameStartTimestamp' : [match['info']['gameStartTimestamp']],
        # 'gameEndTimestamp' : [match['info']['gameEndTimestamp']],
        'gameDuration' : [match['info']['gameDuration']],
        'gameMode' : [match['info']['gameMode']],
        'gameType' : [match['info']['gameType']],
        'gameVersion' : [match['info']['gameVersion']],
        'mapId' : [match['info']['mapId']]
    }
    return pd.DataFrame(row_match)

def df_participants_rows(match):
    participants_rows = {
        'partId': [], 'matchId': [],
        'puuid': [],'summonerId': [], 'summonerName': [], 'summonerLevel': [], 'profileIcon': [], 
        # 'eligibleForProgression': [],
        'participantId': [], 'championId': [], 'championName': [], 'championTransform': [], 'statPerksDefense' : [], 'statPerksFlex' : [],
        'statPerksOffense' : [],'primaryStyle1' : [], 'primaryStyle2' : [], 'primaryStyle3' : [], 'primaryStyle4' : [], 'subStyle1' : [],
        'subStyle2' : [], 'individualPosition': [], 'teamPosition': [], 'lane': [], 'role': [],'teamId': [], 'bans' : [], 'win': []
    }
    participants_rows['matchId'] += [match['metadata']['matchId']] * 10
    for participant in match['info']['participants']:
        participants_rows['partId'].append(participant['puuid'] + match['metadata']['matchId'])
        for key, value in participant.items():
            if key in participants_rows.keys():
                participants_rows[key].append(value)
        runes = participant_runes(participant)
        for key, value in runes.items():
            participants_rows[key].append(value)
    participants_rows['bans'] += participants_bans(match)
    for key, value in participants_rows.items():
        if len(value) < 10:
            participants_rows[key] = [np.nan] * 10
    return pd.DataFrame(participants_rows)


def participants_bans(match):
    bans = []
    for i in range(0,2,1):
        for ban in match['info']['teams'][i]['bans']:
            bans.append(ban['championId'])
    return bans

def participant_runes(participant):
    runes = {
        'statPerksDefense' : participant['perks']['statPerks']['defense'],
        'statPerksFlex' : participant['perks']['statPerks']['flex'],
        'statPerksOffense' : participant['perks']['statPerks']['offense'],
        'primaryStyle1' : participant['perks']['styles'][0]['selections'][0]['perk'],
        'primaryStyle2' : participant['perks']['styles'][0]['selections'][1]['perk'],
        'primaryStyle3' : participant['perks']['styles'][0]['selections'][2]['perk'],
        'primaryStyle4' : participant['perks']['styles'][0]['selections'][3]['perk'],
        'subStyle1' : participant['perks']['styles'][1]['selections'][0]['perk'],
        'subStyle2' : participant['perks']['styles'][1]['selections'][1]['perk']
    }
    return runes