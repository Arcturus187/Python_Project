import random
import sys

def testguess():
    global guess
    try:
        guess = int(guess)
    except ValueError:
        print('Try again! But now with a correct input!')
        guess = input()
        testguess()
    
name = str(input('Please input your name: '))
num = random.randint(1, 50)

print('hey ' + name + ', i have a number between 1-50. Take a guess!')
for counter in range(0, 6):
    guess = input('Guess: ')
    testguess()
    if guess < 1 or guess > 50:
        print('The number is between 1-50. Try again!')
    elif guess < num:
        print('Your guess is to small, ' + name + '!')
    elif guess > num:
        print("It's too big ma boii " + name)
    else:
        break

if guess == num:
    print("Hmph.. you're not to bad i guess," + name + ', as much i hate to say this, Your asnwer is correct!')
    input()
    sys.exit()
elif guess != num:
    print('Tsk. Tsk. Tsk. You failed ' + name +', goodbye! The correct answer is: ' + num)
    input()
    sys.exit()
