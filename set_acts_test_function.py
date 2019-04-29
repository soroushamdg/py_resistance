import random
import math
class player():
    def __init__(self,name,act):
        self.name = name
        self.act = act
players = []
for i in range(0,10):
    a = player(str(i),None)
    players.append(a)
    print(f' {i} -> {a.name} ')
print(players)
def setActs():
    global players
    new_list = players
    random.shuffle(new_list)
    random.shuffle(new_list)
    random.shuffle(new_list)
    for i in range(0,math.floor(len(players)*2/3)):
        new_list[i].act = 'resistance'
    for k in range(math.floor(len(players)*2/3),len(players)):
        new_list[k].act = 'spy'
    players = new_list
    del new_list
    for m in range(0,len(players)):
        print(f'{players[m].name} -> {players[m].act}')
    return True
print(setActs())
                   
    
