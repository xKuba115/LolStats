import requests
import json
import math
from flask import Flask,json, render_template, request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import os
app = Flask(__name__)
api = Api(app)

APIKEY = 'RGAPI-6d79be69-95f6-4a0b-9e26-66b20e163eac'
@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/results", methods = ['GET'])
def data():
        args = request.args
        name = args.get('name')
        if args.get('howManyGames') is not None:
            howManyGames = int(args.get('howManyGames'))
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
                    allDoubleKills = allDoubleKills + int(gameData['info']['participants'][i]['doubleKills'])
                    allTrippleKills = allTrippleKills + int(gameData['info']['participants'][i]['tripleKills'])
                    allQuadraKills = allQuadraKills + int(gameData['info']['participants'][i]['quadraKills'])
                    allPentaKills = allPentaKills + int(gameData['info']['participants'][i]['pentaKills'])

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
            'hoursSpent': hoursSpent
        }

        if name is not None:
            return render_template('index.html',
            name= name,
            howManyGames = howManyGames,
            allKills = allKills,
            wins =wins,
            loses = loses,
            allAssists = allAssists,
            allDeaths = allDeaths,
            allQ = allQ,
            allW = allW,
            allE = allE,
            allR = allR,
            allGoldEarned = allGoldEarned,
            allGoldSpent = allGoldSpent,
            allVisionWardsBoughtInGame = allVisionWardsBoughtInGame,
            allTimeSpent = allTimeSpent,
            allDoubleKills = allDoubleKills,
            allTrippleKills = allTrippleKills,
            allQuadraKills = allQuadraKills,
            allPentaKills = allPentaKills,
            winrate = winrate,
            allSpells= allSpells,
            allGoldSpentOnWards=allGoldSpentOnWards,
            secondsSpent= secondsSpent,
            minutesSpent= minutesSpent,
            hoursSpent= hoursSpent)
        else:
            return render_template('index.html',
            name= ' ',
            howManyGames = ' ',
            allKills = ' ',
            wins =' ',
            loses = ' ',
            allAssists = ' ',
            allDeaths = ' ',
            allQ = ' ',
            allW = ' ',
            allE = ' ',
            allR = ' ',
            allGoldEarned = ' ',
            allGoldSpent = ' ',
            allVisionWardsBoughtInGame = ' ',
            allTimeSpent = ' ',
            allDoubleKills = ' ',
            allTrippleKills = ' ',
            allQuadraKills = ' ',
            allPentaKills = ' ',
            winrate = ' ',
            allSpells= ' ',
            allGoldSpentOnWards=' ',
            secondsSpent= ' ',
            minutesSpent= ' ',
            hoursSpent= ' ')
    

if __name__ == '__main__':
    app.run()  

