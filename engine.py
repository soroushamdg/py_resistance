'''
https://en.wikipedia.org/wiki/The_Resistance_(game)
    here we define our objects
'''
from random import shuffle
import random
import datetime
import math
import ast
import os
from os import system, name
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
def clear():
    if os.name == 'nt':
        os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')
def generate_id(obj):
    return str(obj) + datetime.datetime.now().strftime("%YHIMS")
class obj_player():
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
                if vote.lower() == 'fail' or vote == 'pass':
                    return vote
                    break
                else:
                    print('Bad language, you can just type : pass or fail, please try again.')
                    continue
        elif self.act == 'resistance':
            while True:
                vote = input(f'player {self.name} you should vote ONLY for PASS:')
                if vote.lower() == 'pass':
                    return vote
                    break
                else:
                    print('Bad language, you can just type : pass or fail please try again.')
                    continue

class obj_mission():
    """ mission object will containt : result - voters ids - votes"""

    def __init__(self, m_ID,m_leader, m_voters_names,m_voters):
        self.id = m_ID
        self.leader = m_leader
        self.voters_names = m_voters_names
        self.voters = m_voters
        self.result = None
    def __str__(self):
        return 'player {self.leader} defined this mission with following players :'.formant(*self.voters_names,sep='\n')

    def askForMissionVote(self):
        '''
            This function will ask leader if all other players are ok with the mission, it will return True or False
        '''
        vote = input('Is everybody okay with the mission with {} ?(Y/N)'.format(' ,'.join(self.voters_names)))
        if vote.lower() == 'y':
            return True
        else:
            return False

    def startMission(self):
        '''
         This function will start mission and ask in-mission players for their votes.
        '''
        votes = []
        for player in voters:
            votes.append(player.voteForMission())
        for vote in votes:
            if vote.lower() == 'fail':
                self.result = 'FAIL'
                return False
        self.result = 'PASS'
        return True

class next_mission_leader():
    """This object will controll who will lead next mission and how many players should have in mission"""

    def __init__(self, n_players):
        self.players = n_players
        self.round = 0

    def __str__(self):
        return nextLeader()
    def setup(self):
        shuffle(self.players)
    def nextLeader(self):
        round += 1
        return players[round % len(players)].name



class resistanceEngine(object):
    """docstring for resistanceEngine.
    This class is the main core of the game.
    """
    mission_soldier_law = [[],[0,0,0,0,0,2,2,2,3,3,3],[0,0,0,0,0,3,3,3,4,4,4],[0,0,0,0,0,2,4,3,4,4,4],[0,0,0,0,0,3,3,4,5,5,5],[0,0,0,0,0,3,4,4,5,5,5]]
    def __init__(self):
        self.players = []
        self.missions = []

    def setupNewPlayer(self):
        if len(self.players) <= 10:
            name = input("Please write new player's name : ")
            id = generate_id('p')
            self.players.append(obj_player(id,name,'UNKNOWN'))
            print(f"{name} added! :D")
            return True
        else:
            print("You have maximum players")
            return False
    def print_players(self):
        for player in self.players:
            print(player.name)
    #should really change it
    def setActs(self):
        if len(self.players) <= 10 and len(self.players) >= 5:
            new_list = self.players
            shuffle(new_list)
            shuffle(new_list)
            shuffle(new_list)
            for i in range(0,math.floor(len(self.players)*2/3)):
                new_list[i].act = 'resistance'
            for k in range(math.floor(len(self.players)*2/3),len(self.players)):
                new_list[k].act = 'spy'
            self.players = new_list
            return True
        elif len(self.players) >= 10:
            print("you have too much players, maximum is 10.")
            return False
        else:
            print("you don't have enough players.")
            return False
    def print_board(self):
        print ('\n')
        print(color.BOLD + color.RED + 'ROUND : '+next_mission_leader_generator.round + color.END)
        mission_board = '\t'+ f"{mission.result for mission in self.missions}"
        print (mission_board)
        print ('_'*len(mission_board))
        print('\nPLAYERS : ')
        for player in self.players:
            print(player.name)
            print ('_'*len(mission_board))

    def start(self):
        if self.setActs() == True:
            next_mission_leader_generator = next_mission_leader(self.players)
            next_mission_leader_generator.setup()
            while(len(self.missions)<5):
                clear()
                while True:
                    clear()
                    self.print_board()
                    new_mission = obj_mission(m_id=generate_id('m'),
                        m_leader=next_mission_leader_generator.nextLeader(),
                        m_voters_names=None,
                        m_voters=None)
                    while True:
                        print('\t'*2+color.BOLD+color.YELLOW+'The Leaders is : \n'+color.END+'\t'*2+new_mission.leader)
                        print('\t'*2+f'You choose {mission_soldier_law[len(self.players)][len(self.missions)]} players')
                        print('Please choose you\'d you like to go to mission?')
                        z = 0
                        for player in self.players:
                            print(f'{z}. {player.name}')
                        z += 1
                        input_mission_players = input('input player indexes like -> [3,2,5] : ')
                        list_mission_players = ast.literal_eval(input_mission_players)
                        #here checks if user entered enough players
                        if len(list_mission_players) != mission_soldier_law[len(self.players)][len(self.missions)]:
                            clear()
                            continue
                        new_mission.voters = [self.players[i-1] for i in list_mission_players]
                        new_mission.voters_names = [player.name for player in new_mission.voters]
                        break
                    if new_mission.askForMissionVote() == False:
                        continue
                    else:
                        clear()
                        if new_mission.startMission() == True:
                            clear()
                            print(color.BOLD + color.GREEN + '\t'*2 + 'MISSION SUCCEEDED'+color.END)
                        else:
                            print(color.BOLD + color.RED + '\t'*2 + 'MISSION FAILED'+color.END)
                        self.missions.append(new_mission)
                    if len(self.missions) == 5 :
                        break
            else:
                self.print_board()
                #here engine checks final results if spies or resistances won.
                pass
        else:
            return
