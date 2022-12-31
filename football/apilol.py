import requests
import json

headers = { 'X-Auth-Token': 'bd93962d45c9409bbadbf0d29c25e67e' }

def historyEPL():
    uri = 'https://api.football-data.org//v4/competitions/PL'
    response = requests.get(uri, headers=headers) # history

    for x in  response.json()['seasons']:
        if (x['winner'] != None):
            print(x['winner']['name'])

def standingS():
    uri = 'https://api.football-data.org/v4/competitions/2021/standings'
    response = requests.get(uri, headers=headers) # standing of current season
    total_type_all = response.json()['standings'][0]
    standings = total_type_all['table']
    return total_type_all['table']
    # for teams in standings:
    #     inside = teams['team']
        # form = teams['form'].replace(","," ")
        # print(type(list(form)))
    #     print(teams['position'], inside['name'],teams['playedGames'], teams['won'], teams['lost'],teams['draw'],teams['points'], form)
# standingS()

def scorer():
    uri = "https://api.football-data.org/v4/competitions/PL/scorers"
    response = requests.get(uri, headers=headers)
    dates = response.json()['season']
    scorers = response.json()['scorers']
    return dates, scorers
    # print(dates['startDate'],dates['endDate'])
    # i = 0
    # for x in scorers:
    #     print(x['player']['name'],x['team']['name'],x['goals'])
    #     i +=1
    #     if i ==5:
    #         return
# scorer()