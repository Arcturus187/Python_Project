def calc_sign(sign):
    if sign.count('-') % 2 == 1:
        return '-'
    else:
        return '+'


def calc_string(num_string):
    if num_string == '':
        pass
    elif num_string == '/exit':
        print('Bye !')
        exit()
    elif num_string == '/help':
        pass
    else:
        num_list = num_string.split()
        if len(num_list) == 1:
            try:
                print(int(num_list[0]))
            except:
                print('Invalid input!')
        else:
            result_box = []
            result_box.append(int(num_list[0]))
            for i in range(1, len(num_list), 2):
                tmp_list = num_list[i:i + 2]
                if calc_sign(tmp_list[0]) == '+':
                    result_box.append(int(tmp_list[1]))
                else:
                    result_box.append(int(tmp_list[1]) * -1)
            print(sum(result_box))


def calculator():
    while True:
        calc_string(input())


calculator()
