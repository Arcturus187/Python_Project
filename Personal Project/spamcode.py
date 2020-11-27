import pyautogui

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0

while True:
    the_text = input('Input the spam text: ')
    if the_text == '/exit':
        break
    else:
        n = input('How many times?: ')
        for i in range(int(n)):
            pyautogui.click(608, 695)
            pyautogui.typewrite(f'{the_text}\n')
