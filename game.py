import engine
import resistanceEngine
import color
import clear
import generate_id, obj_player, obj_mission, next_mission_leader

commander = resistanceEngine()
while True:
    clear()
    print(color.BOLD + color.CYAN + '\t'*2 + 'Welcome to PyResistance' + color.END)
    print(color.CYAN + '\t'*2 + 'you should have 5 to 10 players, use following commands to add players and start the game.' + color.END)
    command = input('<start> the game or <add_players> ?')
    if command == '<start>':
        commander.start()
    elif command == '<add_players>':
        commander.setupNewPlayer()
    else:
        print('Wrong command, please try again.')
