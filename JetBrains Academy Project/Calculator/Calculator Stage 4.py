def main_menu():
    while True:
        cursor = input()
        if cursor == '/exit':
            print('Bye !')
            break
        elif cursor == '/help':
            print('_______')
            continue
        elif cursor == '':
            continue
        else:
            print(calc_plusmin(cursor))


def calc_sign(x):
    minus_count = x.count('-')
    if minus_count % 2 == 0:
        return '+'
    else:
        return '-'


def list_calc(the_list):
    sum_list = []
    for i in range(len(the_list) - 2):
        use_list = the_list[i:i + 3]
        if use_list[1] == '+':
            sum_list.append(int(use_list[0]) + int(use_list[2]))
        else:
            sum_list.append(int(use_list[0]) - int(use_list[2]))
    return sum(sum_list)


def calc_plusmin(num):
    num = num.split()
    if len(num) == 1:
        return num[0]
    else:
        for operator_index in range(1, len(num), 2):
            num[operator_index] = calc_sign(num[operator_index])
        return list_calc(num)


main_menu()
