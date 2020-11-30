import collections


var_storage = {}
operators = {'|': 0,
             '(': 5,
             ')': 5,
             '^': 2,
             '*': 3,
             '/': 3,
             '+': 4,
             '-': 4}
sign_convert = {'--': '+',
                '++': '+',
                '+-': '-',
                '-+': '-'
                }


def peek_stack(stack):
    if len(stack) != 0:
        return stack[-1]
    else:
        return '|'


def covert_math_str_list(math_str):
    math_str = math_str.replace(' ', '')
    math_list = list(math_str)
    for i in range(len(math_list)):
        if math_list[i] in operators:
            math_list[i] = f' {math_list[i]} '
    math_list = ''.join(math_list).split()
    return math_list


def convert_rpn(num_list):
    output_stack = collections.deque()
    operator_stack = collections.deque()
    n = len(num_list)
    for i in range(n):
        item = num_list[i]
        if item.isnumeric():
            output_stack.append(item)
        elif item in operators and len(operator_stack) == 0:
            operator_stack.append(item)
        elif item  == '(':
            operator_stack.append(item)
        elif item == ')':
            while True:
                pop_item = operator_stack.pop()
                if pop_item == '(':
                    break
                else:
                    output_stack.append(pop_item)
        elif item in operators and peek_stack(operator_stack) == '(':
            operator_stack.append(item)
        elif item in operators and operators[item] < operators[peek_stack(operator_stack)]:
            operator_stack.append(item)
        elif item in operators and not operators[item] < operators[peek_stack(operator_stack)]:
            while not operators[item] < operators[peek_stack(operator_stack)]:
                if len(operator_stack) == 0:
                    break
                output_stack.append(operator_stack.pop())
            operator_stack.append(item)

    n = len(operator_stack)
    for _ in range(n):
        output_stack.append(operator_stack.pop())

    return output_stack


def calculate_rpn(rpn_stack):
    calc_stack = collections.deque()
    while True:
        try:
            i = rpn_stack.popleft()
            if i.isnumeric():
                calc_stack.append(float(i))
            elif i in operators:
                b = calc_stack.pop()
                a = calc_stack.pop()
                calc_stack.append(sub_calc(a, b, i))
        except:
            break

    return calc_stack[0]


def sub_calc(a, b, operator):
    if operator == '^':
        return a ** b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    elif operator == '-':
        return a - b
    elif operator == '+':
        return a + b


def assign_var(var, val):
    assign_box = []
    assign_cond = []
    if var.isalpha():
        assign_cond.append(True)
        assign_box.append(var)
    else:
        assign_cond.append(False)
    if val.isalpha() and return_var(val):
        assign_box.append(return_var(val))
        assign_cond.append(True)
    elif val.isdecimal():
        assign_box.append(val)
        assign_cond.append(True)
    else:
        assign_cond.append(False)

    if assign_cond[0] and assign_cond[1]:
        var_storage[assign_box[0]] = assign_box[1]
    elif not assign_cond[0]:
        print('Invalid identifier')
    elif assign_cond[0] and not assign_cond[1]:
        print('Invalid assignment')


def declare_var(var):
    if not var.isalpha():
        print('Invalid identifier')
    elif var not in var_storage:
        print('Unknown variable')
    else:
        print(var_storage[var])


def return_var(var):
    if var in var_storage:
        return int(var_storage[var])
    else:
        return None


def command_menu(text):
    if text == '/exit':
        print('Bye!')
        exit()
    elif text == '/help':
        print('HELP TEXT PLACEHOLDER')
    else:
        print('Unknown command')


def calculate(text):
    n = len(text)
    var_name = ''
    for i in range(n):
        if text[i].isalpha():
            var_index = i
            if i == (n - 1):
                var_name += text[i]
            else:
                while text[var_index].isalpha():
                    var_name += text[var_index]
                    var_index += 1
            text = text.replace(var_name, f'{return_var(var_name)} ')
            var_name = ''

    text = text.replace(' ', '')
    for keys in sign_convert:
        while keys in text:
            text = text.replace(keys, sign_convert[keys])
    print(int(calculate_rpn(convert_rpn(covert_math_str_list(text)))))


def main_calc(text):
    if text == '':
        pass
    elif '=' in text:
        eq_count = text.count('=')
        if eq_count == 1:
            text = text.replace(' ', '')
            var, val = text.split('=')
            assign_var(var, val)
        else:
            print('Invalid assignment')
    elif len(text.split()) == 1:
        if text.isnumeric():
            print(text)
        elif text[0] == '/':
            command_menu(text)
        else:
            declare_var(text)
    else:
        if text.count('(') != text.count(')'):
            print('Invalid expression')
        else:
            calculate(text)


while True:
    main_calc(input().lstrip(' '))