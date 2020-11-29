operators = {'|': 0,
             '(': 5,
             ')': 5,
             '^': 2,
             '*': 3,
             '/': 3,
             '+': 4,
             '-': 4}

def calc_sign(sign_str):
    if '+' in sign_str:
        if '-' in sign_str:
            if sign_str.count('-') % 2 == 0:
                return '+'
            if sign_str.count('-') % 2 == 1:
                return '-'
        else:
            return '+'
    elif '-' in sign_str:
        if sign_str.count('-') % 2 == 0:
            return '+'
        if sign_str.count('-') % 2 == 1:
            return '-'
    else:
        raise Exception

def calculate(text):
    text = text.replace(' ', '')
    tmp_list = list(text)
    n = len(tmp_list)
    for i in range(n):
        if i == (n - 1):
            continue
        elif tmp_list[i].isnumeric():
            if tmp_list[i+1].isnumeric():
                continue
            else:
                tmp_list[i] = f'{tmp_list[i]} '
        else:
            if tmp_list[i + 1].isnumeric():
                tmp_list[i] = f'{tmp_list[i]} '
    text = ''.join(tmp_list)
    tmp_list = text.split()

    for i in range(len(tmp_list)):
        if '+' in tmp_list[i] or '-' in tmp_list[i]:
            tmp_list[i] = calc_sign(tmp_list[i])
    math_str = ' '.join(tmp_list)
    return math_str
while True:
    print(calculate(input()))