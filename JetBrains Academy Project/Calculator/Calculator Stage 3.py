while True:
    num = input()
    if num == '/exit':
        break
    elif num == '/help':
        print('The program calculates the sum of numbers')
    elif num == '':
        continue
    else:
        num = num.split()
        int_num = [int(x) for x in num]
        print(sum(int_num))
print('Bye !')