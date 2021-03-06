import json
import datetime

import numpy as np
from slugify import slugify

import constants


def read_player_data(season=None):
    with open('./data/players-by-team.json') as json_file:
        data = json.load(json_file)

    data = assign_guids(data)

    for _, player in data.items():
        player['general position'] = assign_general_position(player['position'])
        player['season'] = assign_season_to_player(player['url'])

    if season is not None:
        data = {guid: player_details for guid, player_details in data.items() if player_details['season'] == season}

    assert data, "No match lineups to return, have you selected a valid season?"

    return data


def read_match_data(season=None, sort=True):
    with open('./data/match-lineups-with-odds.json') as json_file:
        data = json.load(json_file)

    for match in data:
        match['info']['season'] = assign_season_to_match(match['info']['date'])

    for match in data:
        match['info']['season'] = assign_season_to_match(match['info']['date'])

    if season is not None:
        data = [match for match in data if match['info']['season'] == season]

    if sort:
        for match in data:
            match['info']['datetime'] = convert_date_to_datetime_object(match['info']['date'])
        data = sorted(data, key=lambda x: x['info']['datetime'])

    assert data, "No match lineups to return, have you selected a valid season?"

    return data


def read_fixtures_data():
    with open('./crawler/fixtures.json') as jsonfile:
        fixtures = json.load(jsonfile)

    for fixture in fixtures:
        fixture['datetime'] = convert_date_to_datetime_object(fixture['date'], string_format='%d.%m.%Y')

    fixtures = sorted(fixtures, key=lambda x: x['datetime'])

    return fixtures


def normalise_features(vector):
    assert isinstance(vector, np.ndarray)
    return ((vector - 50) / (100 - 50)).clip(min=0)


def convert_date_to_datetime_object(date, string_format='%d %B %Y'):
    return datetime.datetime.strptime(date, string_format)


def assign_season_to_match(date):

    date = convert_date_to_datetime_object(date)

    year = date.year
    month = date.month
    if month in [7, 8, 9, 10, 11, 12]:
        season = str(year) + '-' + str(year + 1)
    else:
        season = str(year - 1) + '-' + str(year)
    return season


def assign_season_to_player(url):
    url = url.split('/')[-2]
    season = constants.PLAYER_URL_TO_SEASON.get(url, '2017-2018')
    return season


def assign_guids(data):
    for i, player in enumerate(data):
        player['guid'] = i
    guid_conversion = {player['guid']: player for player in data}
    return guid_conversion


def assign_general_position(position):
    return constants.EXACT_TO_GENERIC[position]


def assign_odds_to_match(matchlineups, fd):
    for match in matchlineups:
        for index, row in fd.iterrows():
            try:
                home_team = constants.FOOTBALL_DATA_TEAM_MAPPINGS['2014-2015'][match['info']['home team']]
                away_team = constants.FOOTBALL_DATA_TEAM_MAPPINGS['2014-2015'][match['info']['away team']]

            except KeyError:
                home_team = None
                away_team = None

        if home_team == slugify(row['HomeTeam']) and away_team == slugify(row['AwayTeam']):
            if datetime.datetime.strptime(match['info']['date'], '%d %B %Y') == datetime.datetime.strptime(row['Date'], '%d/%m/%y'):
                match['info']['home odds'] = row['PSH']
                match['info']['draw odds'] = row['PSD']
                match['info']['away odds'] = row['PSA']

    return matchlineups


def get_goals(match):
    return match['info']['home goals'], match['info']['away goals']


def get_season(match):
    return match['info']['season']


def get_lineup_names(match):
    return match['info']['home lineup names'], match['info']['away lineup names']


def get_teams(match):
    return constants.LINEUP_TO_PLAYER_TEAM_MAPPINGS['ALL'][match['info']['home team']], \
           constants.LINEUP_TO_PLAYER_TEAM_MAPPINGS['ALL'][match['info']['away team']]


def get_lineup_numbers(match):
    return match['info']['home lineup numbers'], match['info']['away lineup numbers']


def get_lineup_nationalities(match):
    return match['info']['home lineup nationalities'], match['info']['away lineup nationalities']


def get_match_odds(match):
    return match['info']['home odds'], match['info']['draw odds'], match['info']['away odds']