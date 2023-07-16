import requests
import json

#token
headers = { 'X-Auth-Token': 'bd93962d45c9409bbadbf0d29c25e67e' }

def standingS():
    uri = 'https://api.football-data.org/v4/competitions/PL/standings'
    response = requests.get(uri, headers=headers) # standing of current season
    total_type_all = response.json()['standings'][0]
    standings = total_type_all['table']
    return standings

def scorer():
    uri = "https://api.football-data.org/v4/competitions/PL/scorers"
    response = requests.get(uri, headers=headers)
    dates = response.json()['season']
    scorers = response.json()['scorers']
    return dates, scorers

def todayMatch():
    uri="https://api.football-data.org/v4/competitions/PL/matches?status=SCHEDULED"
    response = requests.get(uri, headers=headers)
    matches = response.json()['matches'] # list of dict
    return matches

def teamStats():
    uri="http://api.football-data.org/v4/competitions/PL/teams"
    response = requests.get(uri, headers=headers)
    teams = response.json()['teams']
    return teams