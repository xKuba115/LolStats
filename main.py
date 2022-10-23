import requests
import json
import math

APIKEY = 'RGAPI-6d79be69-95f6-4a0b-9e26-66b20e163eac'
name = 'BreaDoggy'
howManyGames = 5
allKills = 0
wins =0
loses = 0
allabilityUsed = 0
allAssists = 0
allDeaths = 0
allQ = 0
allW = 0
allE = 0
allR = 0
allSpells = 0
allGoldEarned = 0
allGoldSpent = 0
allVisionWardsBoughtInGame = 0
allTimeSpent = 0

r = requests.get(f'https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key={APIKEY}')
summonerData = r.json()
summonerPUUID = summonerData['puuid']
summonerName = summonerData['name']
summoneraccountId = summonerData['accountId']


r1 = requests.get(f'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{summonerPUUID}/ids?count={howManyGames}&api_key={APIKEY}')
summonerGames = r1.json()


for x in range(howManyGames):
    game = summonerGames[x]
    r2 = requests.get(f'https://europe.api.riotgames.com/lol/match/v5/matches/{game}?api_key={APIKEY}')
    gameData = r2.json()
    for i in  range(10):
        checkId = gameData['info']['participants'][i]['puuid']
        if(checkId == summonerPUUID):
            if (gameData['info']['participants'][i]['win'] == 0):
                didWin = "lose"
                loses = loses +1
            else:
                didWin = "win"
                wins = wins+1

            allAssists = allAssists + int(gameData['info']['participants'][i]['assists'])
            allKills = allKills + int(gameData['info']['participants'][i]['kills'])
            allDeaths = allDeaths + int(gameData['info']['participants'][i]['deaths'])
            allQ = allQ + int(gameData['info']['participants'][i]['spell1Casts'])
            allE = allE + int(gameData['info']['participants'][i]['spell2Casts'])
            allW = allW + int(gameData['info']['participants'][i]['spell3Casts'])
            allR = allR + int(gameData['info']['participants'][i]['spell4Casts'])
            allGoldEarned = allGoldEarned + int(gameData['info']['participants'][i]['goldEarned'])
            allGoldSpent = allGoldSpent + int(gameData['info']['participants'][i]['goldSpent'])
            allVisionWardsBoughtInGame = allVisionWardsBoughtInGame + int(gameData['info']['participants'][i]['visionWardsBoughtInGame'])
            allTimeSpent = allTimeSpent + int(gameData['info']['gameDuration'])
        i=i+1
        
    x=x+1
winrate =round( (wins/(wins+loses))*100,2)
allSpells = allQ + allW + allE + allR
allGoldSpentOnWards = allVisionWardsBoughtInGame *75
secondsSpent = allTimeSpent%60
minutesSpent = math.floor(allTimeSpent/60)
hoursSpent = math.floor(minutesSpent/60)
print("----------------------")
print(f"{summonerName} stats in last {howManyGames} games")
print (f"Time spent in game:{hoursSpent}h {minutesSpent - hoursSpent*60 }m {secondsSpent}s")

print("----------------------")
print("General section")
print("----------------------")
print (f"All kills in last {howManyGames} games: {allKills}")
print (f"All deaths in last {howManyGames} games: {allDeaths}")
print (f"All assists in last {howManyGames} games: {allAssists}")
print (f"Winrate in last  {howManyGames} games: {winrate}%")
print("----------------------")
print("Spells section")
print("----------------------")
print (f"All spells casted in last {howManyGames} games: {allSpells}")
print(f"Q: {allQ}")
print(f"W: {allW}")
print(f"E: {allE}")
print(f"R: {allR}")
print("----------------------")
print("Gold section")
print("----------------------")
print (f"Gold earned in last {howManyGames} games: {allGoldEarned}")
print (f"Gold spent in last {howManyGames} games: {allGoldSpent}")
print (f"Gold spent on wards in last {howManyGames} games: {allGoldSpentOnWards}")
print("----------------------")

