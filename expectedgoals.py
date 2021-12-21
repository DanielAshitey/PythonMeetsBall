import random

HomexG = [0.6,0.7,0.8]
AwayxG = [0.2,0.3,0.32,0.11,0.26,0.27,0.24,0.19,0.22]

def findwinner(HomexG,AwayxG):
    HomeGoals = 0
    AwayGoals = 0

    for i in HomexG:
        x = random.uniform(0,1)
        if x <= i:
            HomeGoals = HomeGoals + 1

    for j in AwayxG:
        y = random.uniform(0,1)
        if y <= j:
            AwayGoals = AwayGoals + 1

    if HomeGoals > AwayGoals:
        return("Home win")
    elif HomeGoals < AwayGoals:
        return("Away win")
    else:
        return("Draw")

def iter(hometeam,awayteam):
    Homecount = 0
    Awaycount = 0
    Drawcount = 0

    for i in range(0,5000):
        result = findwinner(hometeam,awayteam)
        if result == "Home win":
            Homecount = Homecount + 1
        elif result == "Away win":
            Awaycount = Awaycount + 1
        else:
            Drawcount = Drawcount + 1

    HomeWinPercentage = (Homecount/5000)*100
    AwayWinPercentage = (Awaycount/5000) * 100
    DrawPercentage = (Drawcount/5000) * 100
    print("Home win percentage = " + str(HomeWinPercentage) + "%")
    print("Away win percentage = " + str(AwayWinPercentage) + "%")
    print("Draw percentage = " + str(DrawPercentage) + "%")

iter(HomexG,AwayxG)
