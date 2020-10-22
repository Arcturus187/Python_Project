import random

def roshambo():
    opt = ['scissors', 'paper', 'rock']
    cpu_opt = random.choice(opt)
    player_opt = input()
    
    result_dict = { 'paper': {'paper': 'draw', 'rock': 'win', 'scissors': 'lose'},
                    'rock': {'paper': 'lose', 'rock': 'draw', 'scissors': 'win'},
                    'scissors': {'paper': 'win', 'rock': 'lose', 'scissors': 'draw'}}
    if result_dict[player_opt][cpu_opt] == 'win':
        return f'Well done. The computer choose {cpu_opt} and failed'
    elif result_dict[player_opt][cpu_opt] == 'lose':
        return f'Sorry, but the computer choose {cpu_opt}'
    elif result_dict[player_opt][cpu_opt] == 'draw':
        return f'There is a draw ({cpu_opt})'
    else:
        return 'Wrong input!'
        
print(roshambo())
