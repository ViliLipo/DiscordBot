
import requests
import re


skilltable = ["Total","Attack", "Defence", "Strength", \
"Hp", "Ranged","Prayer","Magic", "Cooking", "Woodcutting", \
"Fletching", "Fishing", "Firemaking", "Crafting", \
"Smithing", "Mining", "Herblore", "Agility", \
"Thieving", "Slayer", "Farming", "Runecraft", "Hunter", \
"Construction"]


class Skill:
    def __init__(self, index):
        self.name = skilltable[index]
        #print(self.name)
        self.rank = 0
        self.exp = 0
        self.level = 0
    def __str__(self):
        #text = (self.name + " Rank: " + str(self.rank) + " Experience: " + str(self.exp) + " Level: " + str(self.level))
        text = '|{0:12}|{1:7}|{2:8}|{3:5}|'.format(self.name, str(self.rank), str(self.exp), str(self.level))
        text = text + "\n ------------------------------------"
        return text

class Player:
    def __init__(self, playername):
        self.name = playername
        self.skills = []
    def shortMessage(self):
        print("shortMessage")
        message = self.name + "'s OSRS Hi Scores'\n" + '|{0:12}|{1:7}|{2:8}|{3:5}|'.format("Skill", "Rank", "XP", "Level")
        message = message +  "\n ------------------------------------"
        message = message +"\n" + str(self.skills[0])
        return message
    def longMessage(self):
        message = self.name + "'s OSRS Hi Scores'\n" + '|{0:12}|{1:7}|{2:8}|{3:5}|'.format("Skill", "Rank", "XP", "Level")
        message = message +  "\n ------------------------------------\n"
        for skill in self.skills:
            message = message + str(skill) + "\n"
        return message


def osrs_request_player(playername):
    print("Fetching")
    API_ENDPOINT = "http://services.runescape.com/m=hiscore_oldschool/index_lite.ws"
    PARAMS = {'player':playername}
    r = requests.get(url=API_ENDPOINT, params=PARAMS)
    if (r.status_code != 200):
        raise Exception('Can not find find {playername}')
        return
    print("got 200")
    content = (r.text)
    if content == "":
        raise Exception('Can not find find {playername}')
        return
    #print(content)
    player = Player(playername)

    #print(content)
    lines = content.split('\n')

    datatable = []

    for i in range(0, len(skilltable)):
        line = lines[i]
        txtline = line.split(',')
        skill = Skill(i)
        skill.rank = int(txtline[0])
        skill.level = int(txtline[1])
        skill.exp = int(txtline[2])
        player.skills.append(skill)

    return player

def testdriver():
    player = osrs_request_player("Klassi")
    print(player.shortMessage())
    print(player.longMessage())


#testdriver()
