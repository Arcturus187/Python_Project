# Reverse Infix notation to Postfix (Reverse Polish Notation)
import collections

test_case = input()
operators = {'|': 0,
             '(': 5,
             ')': 5,
             '^': 2,
             '*': 3,
             '/': 3,
             '+': 4,
             '-': 4}

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
    print(math_list)
    while math_list.count('(') != math_list.count(')'):
        math_list.append(')')
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
        else:
            raise Exception

    n = len(operator_stack)
    for _ in range(n):
        output_stack.append(operator_stack.pop())

    return output_stack


def calculate_rpn(rpn_stack):
    calc_stack = collections.deque()
    while len(rpn_stack) != 0:
        i = rpn_stack.popleft()
        if i.isnumeric():
            calc_stack.append(float(i))
        elif i in operators:
            b = calc_stack.pop()
            a = calc_stack.pop()
            calc_stack.append(sub_calc(a, b, i))
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


print(calculate_rpn(convert_rpn(covert_math_str_list(test_case))))