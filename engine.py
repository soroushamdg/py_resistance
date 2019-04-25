'''
https://en.wikipedia.org/wiki/The_Resistance_(game)
    here we define our objects
'''
from random import shuffle
import random
import datetime
import math
def generate_id(obj):
    return str(obj) + datetime.datetime.now().strftime("%YHIMS")
class player():
    """
        player object contains : name - act
    """

    def __init__(self, p_id,p_name, p_act):
        self.id = p_id
        self.name = p_name
        self.act = p_act
        self.votes = []
        self.missionsIDs = []
    def __str__(self):
        return f'player {self.name} is {self.act}'

    def voteForMission(self):
        '''
         this method will ask player to vote for the mission and will return result in string.
        '''
        if self.act == 'spy':
            while True:
                vote = input(f'player {self.name} you should vote for PASS or FAIL :')
                if vote.lowercase() == 'fail' or vote == 'pass':
                    return vote
                    break
                else:
                    print('Bad language, please try again.')
                    continue
        elif self.act == 'resistance':
            while True:
                vote = input(f'player {self.name} you should vote ONLY for PASS:')
                if vote.lowercase() == 'pass':
                    return vote
                    break
                else:
                    print('Bad language, please try again.')
                    continue

class mission():
    """ mission object will containt : result - voters ids - votes"""

    def __init__(self, m_ID,m_leader, m_voterIDs):
        self.id = m_ID
        self.leader = m_leader
        self.voterIDs = m_voterIDs

    def __str__(self):
        return f'player {self.leader} defined this misson with following players :\n {player.name for player in self.voterIDs}'

    def askForMissionVote(self):
        '''
            This function will ask leader if all other players are ok with the mission, it will return True or False
        '''
        vote = input(f'Is everybody okay with the mission with {player.name for player in self.voterIDs} following players?(Y/N)')
        if vote.lowercase() == 'y':
            return True
        else:
            return False

    def startMission(self):
        '''
         This function will start mission and ask in-mission players for their votes.
        '''
        votes = []
        for player in voterIDs:
            votes.append(player.voteForMission())
        for vote in votes:
            if vote.lowercase() == 'fail':
                return False
        return True

class nextMissionLeader():
    """This object will controll who will lead next mission and how many players should have in mission"""

    def __init__(self, n_players):
        self.players = n_players
        self.round = 0

    def __str__(self):
        return nextLeader
    def setup(self):
        shuffle(self.players)
    def nextLeader(self):
        return players[round % count(players)].name



class resistanceEngine(object):
    """docstring for resistanceEngine.
    This class is the main core of the game.
    """

    def __init__(self):
        self.players = {}
        self.missions = {}

    def setupNewPlayer():
        if count(players.keys) <= 10:
            name = input("Please write new player's name : ")
            id = generate_id('p')
            players[id] = player(id,name,'UNKNOWN')
            print(f"{name} added! :D")
            return True
        else:
            print("You have maximum players")
            return False
    def players():
        for player in players.values:
            print(player.name)
    def setActs():
        if count(players) <= 10 and count(players) >= 5:
            full = players.keys
            selected = []
            for i in range(0,math.floor(count(players)*2/3)):
                sid = random.choice(full)
                selected.append(sid)
                players[sid].act = 'RESISTANCE'
                full.remove(sid)
            for i in full:
                sid = i
                selected.append(sid)
                players[sid].act = 'SPY'
                full.remove(sid)
            return True
        else:
            print("you don't have enough players")
            return False
    def print_board():
        pass
    def start():
        while True:
            input = input("what to do?")
