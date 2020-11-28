var_storage = {}

TO_DO = '''
TO DO LIST:
1. ASSIGN VARIABLE (done)
    a. input variable only 
        name need to be valid (is alpha only)
    b. If a variable is valid but not declared yet, the program should print "Unknown variable" 
    c. If there is '=' more than 1, or assign invalid variable to a valid one print Invalid assignment

2. COMMAND MENU: (done)
    a. /exit menu print 'Bye!'
    b. /help menu
    c. else: print Unknown Command 

3. CALCULATION (done)
    a. if there is variable in calculation change it to integer
        -check variable name valid or not
        - if valid, is the variable exist?
    b. calculate the list
    
    '''

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

def calc_sign(sign_str):
    if sign_str.count('-') % 2 == 1:
        return '-'
    else:
        return '+'

def calculate(num_str):
    num_list = num_str.split()
    # Variable check
    check_var = True
    for i in range(0, len(num_list), 2):
        if check_var == False:
            pass
        elif not num_list[i].isalpha() and not num_list[i].isnumeric():
            print('Invalid expression')
            check_var = False
        elif num_list[i].isalpha() and num_list[i] not in var_storage:
            print('Unknown variable')
            check_var = False
        elif num_list[i].isnumeric():
            continue
        elif num_list[i].isalpha():
            num_list[i] = return_var(num_list[i])

    if check_var == False:
        pass
    else:
        try:
            result_box = []
            result_box.append(int(num_list[0]))
            for i in range(1, len(num_list), 2):
                tmp_list = num_list[i:i + 2]
                if calc_sign(tmp_list[0]) == '+':
                    result_box.append(int(tmp_list[1]))
                else:
                    result_box.append(int(tmp_list[1]) * -1)
            print(sum(result_box))
        except:
            print('Invalid expression')

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
        calculate(text)

while True:
    main_calc(input())