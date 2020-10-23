import random

def roshambo():
    opt = ['scissors', 'paper', 'rock']
    cpu_opt = random.choice(opt)
    player_opt = input()
    
    if player_opt == '!exit':
        print('Bye!')
        exit()
    elif player_opt not in opt:
        print('Invalid input')
        roshambo()
    
    result_dict = { 'paper': {'paper': 'draw', 'rock': 'win', 'scissors': 'lose'},
                    'rock': {'paper': 'lose', 'rock': 'draw', 'scissors': 'win'},
                    'scissors': {'paper': 'win', 'rock': 'lose', 'scissors': 'draw'}}
    if result_dict[player_opt][cpu_opt] == 'win':
        print(f'Well done. The computer chose {cpu_opt} and failed')
    elif result_dict[player_opt][cpu_opt] == 'lose':
        print(f'Sorry, but the computer chose {cpu_opt}')
    elif result_dict[player_opt][cpu_opt] == 'draw':
        print(f'There is a draw ({cpu_opt})')
        
def play():
    while True:
        roshambo()

play()
