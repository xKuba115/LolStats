import requests
import json
import math
from flask import Flask,json, render_template, request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import os
APIKEY = 'RGAPI-0cf63080-aa93-483e-92af-3436ebc4fc46'
def GetData():
        serv = 'eun1'
        region = 'europe'
        args = request.args
        name = args.get('name')
        if args.get('howManyGames') is not None:
            howManyGames = int(args.get('howManyGames'))
        if (args.get('region')=='EUNE'):
            serv = 'eun1'
            region = 'europe'
        if (args.get('region')=='EUW'):
            serv = 'euw1'
            region = 'europe'
        if (args.get('region')=='NA'):
            serv = 'na1'
            region = 'americas'
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
        allDoubleKills = 0
        allTrippleKills = 0
        allQuadraKills = 0
        allPentaKills = 0
        allBaronKills = 0
        allBountyGold = 0
        allEpicMonsterSteals = 0
        firstBloods = 0
        allInhibitorKills = 0
        alltimeCCingOthers = 0
        totalMinionsKilled = 0
        visionScore = 0


        r = requests.get(f'https://{serv}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key={APIKEY}')
        summonerData = r.json()
        if r.status_code==200:
            summonerPUUID = summonerData['puuid']

        



            r1 = requests.get(f'https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{summonerPUUID}/ids?count={howManyGames}&api_key={APIKEY}')
            summonerGames = r1.json()
            if r1.status_code==200:

                for x in range(howManyGames):
                    game = summonerGames[x]
                    r2 = requests.get(f'https://{region}.api.riotgames.com/lol/match/v5/matches/{game}?api_key={APIKEY}')
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
                            if (gameData['info']['participants'][i]['firstBloodKill'] == 1):
                                
                                firstBloods = firstBloods +1


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
                            allDoubleKills = allDoubleKills + int(gameData['info']['participants'][i]['doubleKills'])
                            allTrippleKills = allTrippleKills + int(gameData['info']['participants'][i]['tripleKills'])
                            allQuadraKills = allQuadraKills + int(gameData['info']['participants'][i]['quadraKills'])
                            allPentaKills = allPentaKills + int(gameData['info']['participants'][i]['pentaKills'])
                            allBaronKills = allBaronKills + int(gameData['info']['participants'][i]['baronKills'])
                            allInhibitorKills = allInhibitorKills + int(gameData['info']['participants'][i]['inhibitorKills'])
                            alltimeCCingOthers = alltimeCCingOthers + int(gameData['info']['participants'][i]['timeCCingOthers'])
                            totalMinionsKilled = totalMinionsKilled + int(gameData['info']['participants'][i]['totalMinionsKilled'])
                            visionScore = visionScore + int(gameData['info']['participants'][i]['visionScore'])
                            if(gameData['info']['gameMode'] == 'ARAM' or gameData['info']['gameMode'] == 'CLASSIC'):
                                allBountyGold = allBountyGold + int(gameData['info']['participants'][i]['challenges']['bountyGold'])
                                allEpicMonsterSteals = allEpicMonsterSteals + int(gameData['info']['participants'][i]['challenges']['epicMonsterSteals'])


                        i=i+1
                        
                    x=x+1
                winrate =round( (wins/(wins+loses))*100,2)
                allSpells = allQ + allW + allE + allR
                allGoldSpentOnWards = allVisionWardsBoughtInGame *75
                secondsSpent = allTimeSpent%60
                hoursSpent = math.floor(allTimeSpent/3600)
                minutesSpent = math.floor(allTimeSpent/60 - hoursSpent *60)        
                allabilityUsed = allQ+allW+allE+allR
                data = {
                    'name': name,
                    'howManyGames' : howManyGames,
                    'allKills' : allKills,
                    'wins' :wins,
                    'loses' : loses,
                    'allAssists' : allAssists,
                    'allDeaths' : allDeaths,
                    'allQ' : allQ,
                    'allW' : allW,
                    'allE' : allE,
                    'allR' : allR,
                    'allSpells' : allSpells,
                    'allGoldEarned' : allGoldEarned,
                    'allGoldSpent' : allGoldSpent,
                    'allVisionWardsBoughtInGame' : allVisionWardsBoughtInGame,
                    'allTimeSpent' : allTimeSpent,
                    'allDoubleKills' : allDoubleKills,
                    'allTrippleKills' : allTrippleKills,
                    'allQuadraKills' : allQuadraKills,
                    'allPentaKills' : allPentaKills,
                    'winrate' : winrate,
                    'allSpells': allSpells,
                    'allGoldSpentOnWards':allGoldSpentOnWards,
                    'secondsSpent': secondsSpent,
                    'minutesSpent': minutesSpent,
                    'hoursSpent': hoursSpent,
                    'allBaronKills' : allBaronKills,
                    'allBountyGold' : allBountyGold,
                    'allEpicMonsterSteals' :allEpicMonsterSteals,
                    'firstBloods':firstBloods,
                    'allInhibitorKills':allInhibitorKills,
                    'alltimeCCingOthers':alltimeCCingOthers,
                    'totalMinionsKilled':totalMinionsKilled,
                    'visionScore':visionScore
                }
            elif r1.status_code==408:
                data = 'Timeout'
        else:
            data = 'Name not found on selected server'
        return data