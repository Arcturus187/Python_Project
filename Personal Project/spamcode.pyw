import pyautogui

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0

MAIN_MENU_TEXT = '''SIMPLE SPAM APP
Click On The Text Box That You Want To Spam First
INSERT SPAM TEXT:'''

SPAM_AMOUNT_TEXT = 'Insert how many times to spam: (limit = 30)'


while True:
    menu_text = pyautogui.prompt(MAIN_MENU_TEXT)
    if menu_text == None:
        exit()
    else:
        while True:
            n_times = pyautogui.prompt(SPAM_AMOUNT_TEXT)
            if n_times == None:
                exit()
            else:
                try:
                    n_times = int(n_times)
                    if n_times > 30 or n_times < 0:
                        raise Exception
                    else:
                        break
                except:
                    pyautogui.alert('Invalid input: Insert only positive whole number not more than 30.')
                    continue
        for i in range(n_times):
            pyautogui.typewrite(f'{menu_text}\n')
