while True:
    num = input()
    if num == '/exit':
        print('Bye !')
        break
    elif num == '':
        continue
    else:
        num = num.split()
        int_num = [int(x) for x in num]
        print(sum(int_num))