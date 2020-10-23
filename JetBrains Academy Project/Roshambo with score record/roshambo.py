import random

name_inp = input('Enter your name: ')
print(f'Hello, {name_inp}')
rating_file = open('rating.txt', 'r+')
rating_dict = {}
player_opt = None
opt = ['scissors', 'paper', 'rock']

for lines in rating_file:
    name, score = lines.split()
    rating_dict[name] = int(score.replace('\n', ''))
if name_inp not in rating_dict.keys():
    rating_dict[name_inp] = 0
rating_file.close()


while True:
    player_opt = input()
    if player_opt == '!exit':
        print('Bye!')
        rating_file = open('rating.txt', 'w')
        update_list = []
        for keys in rating_dict.keys():
            update_list.append(f'{keys} {rating_dict[keys]}')
        for pair in update_list:
            print(pair, end='\n', file=rating_file, flush=True)
        rating_file.close()
        exit()
    elif player_opt == '!rating':
        print(f'Your rating: {rating_dict[name_inp]}')
        continue
    elif player_opt not in opt:
        print('Invalid input')
        continue

    cpu_opt = random.choice(opt)

    result_dict = {'paper': {'paper': 'draw', 'rock': 'win', 'scissors': 'lose'},
                   'rock': {'paper': 'lose', 'rock': 'draw', 'scissors': 'win'},
                   'scissors': {'paper': 'win', 'rock': 'lose', 'scissors': 'draw'}}
    if result_dict[player_opt][cpu_opt] == 'win':
        print(f'Well done. The computer chose {cpu_opt} and failed')
        rating_dict[name_inp] += 100
    elif result_dict[player_opt][cpu_opt] == 'lose':
        print(f'Sorry, but the computer chose {cpu_opt}')
    elif result_dict[player_opt][cpu_opt] == 'draw':
        print(f'There is a draw ({cpu_opt})')
        rating_dict[name_inp] += 50