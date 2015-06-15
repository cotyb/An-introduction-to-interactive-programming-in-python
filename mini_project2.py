#Rock-paper-scissors-lizard-Spock
import random

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        print 'please correct!'
def number_to_name(number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        print 'please correct!'

def rpsls(player_choice):
    print '\nPlayer chooses ' + player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5)
    print 'Computer chooses ' + number_to_name(comp_number)
    if (player_number - comp_number) % 5 == 0:
        print 'Player and Computer tie!'
    elif (((player_number - comp_number) % 5 != 0) and ((player_number - comp_number) % 5 < 3)):
        print 'Player wins!'
    else:
        print 'Computer wins!'
        
     
rpsls('rock')
rpsls('Spock')
rpsls('paper')
rpsls('lizard')
rpsls('scissors')