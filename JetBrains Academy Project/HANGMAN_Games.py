import random
import sys


def main_menu():
    play_exit = ''
    
    while play_exit != 'exit':
        play_exit = input('Type "play" to play the game, "exit" to quit: ')
        if play_exit == 'play':
            the_game()
            
    else:
        sys.exit()

        
def the_game():
    data_choice = ['javascript', 'python', 'java', 'kotlin']
    the_word = random.choice(data_choice)
    all_star = '-' * len(the_word)

    set_check = set(the_word)
    repeat_check = set()
    counter = 0
    guess = ''

    while True:
        if len(set_check) == 0:
            print('''You guessed the word!
    You survived!''')
            print()
            main_menu()
            break
        
        if counter == 8:
            print('You lost!')
            print()
            main_menu()
            break
        
        print()
        print(all_star)
        guess = input("Input a letter: ")
    
        if len(guess) != 1:
            print('You should input a single letter')
            continue
        
        if guess.isupper() or not guess.isalpha():
            print('It is not an ASCII lowercase letter')
            continue
    

        if guess in set_check:
            all_star_check = []
            all_star = list(all_star)
        
            for i in range(len(the_word)):
               if the_word[i] == guess:
                 all_star_check.append(i)
                
            for i in all_star_check:
                all_star[i] = guess
                
            all_star = ''.join(all_star)
            repeat_check.add(guess)
            set_check.discard(guess)
        
        elif guess in repeat_check:
            print("You already typed this letter")
        
        else:
            repeat_check.add(guess)
            print("No such letter in the word")
            counter += 1
    
        

print('H A N G M A N')
main_menu()
