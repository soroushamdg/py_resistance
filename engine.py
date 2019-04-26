'''
https://en.wikipedia.org/wiki/The_Resistance_(game)
    here we define our objects
'''
from random import shuffle
import random
import datetime
import math
import ast
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

    def __str__(self):
        return f'player {self.leader} defined this misson with following players :',*self.voters_names,sep='\n'

    def askForMissionVote(self):
        '''
            This function will ask leader if all other players are ok with the mission, it will return True or False
        '''
        vote = input(f'Is everybody okay with the mission with {} ?(Y/N)'.format(' ,'.join(self.voters_names)))
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
                return False
        return True

class next_mission_leader():
    """This object will controll who will lead next mission and how many players should have in mission"""

    def __init__(self, n_players):
        self.players = n_players
        self.round = 0

    def __str__(self):
        return nextLeader
    def setup(self):
        shuffle(self.players)
    def nextLeader(self):
        round += 1
        return players[round % count(players)].name



class resistanceEngine(object):
    """docstring for resistanceEngine.
    This class is the main core of the game.
    """
    mission_soldier_law = [[],[0,0,0,0,0,2,2,2,3,3,3],[0,0,0,0,0,3,3,3,4,4,4],[0,0,0,0,0,2,4,3,4,4,4],[0,0,0,0,0,3,3,4,5,5,5],[0,0,0,0,0,3,4,4,5,5,5]]
    def __init__(self):
        self.players = []
        self.missions = []

    def setupNewPlayer(self):
        if count(players.keys) <= 10:
            name = input("Please write new player's name : ")
            id = generate_id('p')
            players.append(obj_player(id,name,'UNKNOWN'))
            print(f"{name} added! :D")
            return True
        else:
            print("You have maximum players")
            return False
    def players(self):
        for player in players.values:
            print(player.name)
    #should really change it
    def setActs(self):
        if count(players) <= 10 and count(players) >= 5:
            full = self.players
            selected = []
            for i in range(0,math.floor(count(players)*2/3)):
                sid = random.choice(full)
                selected.append(sid)
                self.players[sid].act = 'RESISTANCE'
                full.remove(sid)
            for i in full:
                sid = i
                selected.append(sid)
                self.players[sid].act = 'SPY'
                full.remove(sid)
            return True
        else:
            print("you don't have enough players")
            return False
    def print_board(self):
        pass
    def start(self):
        if setActs() == True:
            next_mission_leader_generator = next_mission_leader(players.keys)
            while(count(missions)<5):
                clear()
                while True
                    new_mission = obj_mission(m_id=generate_id('m'),m_leader=next_mission_leader_generator.nextLeader(),m_voters_names=[],m_voters=[])
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
                        if len(list_mission_players) != mission_soldier_law[len(players)][len(missions)]:
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




                pass

        else:
            return
