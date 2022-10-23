import requests
import json

apiKey = 'RGAPI-6d79be69-95f6-4a0b-9e26-66b20e163eac'
name = 'Prado'

r = requests.get(f'https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key={apiKey}')
summonerData = r.json()
summonerPUUID = summonerData['puuid']
summonerName = summonerData['name']
summoneraccountId = summonerData['accountId']

r1 = requests.get(f'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{summonerPUUID}/ids?count=5&api_key={apiKey}')
summonerGames = r1.json()
game = summonerGames[0]
r2 = requests.get(f'https://europe.api.riotgames.com/lol/match/v5/matches/{game}?api_key={apiKey}')
gameData = r2.json()

for i in  range(10):
    checkId = gameData['info']['participants'][i]['puuid']
    if(checkId == summonerPUUID):
        print(f"Kills on {gameData['info']['participants'][i]['championName']}: {gameData['info']['participants'][i]['kills']}")
    i=i+1

