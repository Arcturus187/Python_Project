import pyautogui
import time
import random


pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

SPAWN_CREATURE_MENU = '''What creature?
1. dragon
2. dragon priest
3. giant
4. spider'''

MAIN_MENU_TEXT = '''What do you want? (Type the number)
    1. Items
    2. Creatures
    3. Dragon Souls
    4. Increase Skill
    0. Exit'''

AMOUNT_MENU = 'How many?'

ADDITEMS_TEXT = '''What item do you want?
1. gold
2. lockpick'''

SOULS_TEXT = 'How many dragon souls do you want?'

SKILL_TEXT = 'Insert the name of the skill you want to increase!'

SKILL_AMOUNT = 'How many levels?'

def menu():
    menu_index = pyautogui.prompt(MAIN_MENU_TEXT)
    if menu_index == '0':
        exit()
    elif menu_index == '1':
        skyrim_additems(pyautogui.prompt(ADDITEMS_TEXT), pyautogui(AMOUNT_MENU))
    elif menu_index == '2':
        skyrim_spawn(pyautogui.prompt(SPAWN_CREATURE_MENU), pyautogui.prompt(AMOUNT_MENU))
    elif menu_index == '3':
        skyrim_souls(pyautogui.prompt(SOULS_TEXT))
    elif menu_index == '4':
        skyrim_incskill(pyautogui.prompt(SKILL_TEXT), pyautogui.prompt(SKILL_AMOUNT))


def skyrim_spawn(object_name, n):
    object_dict = {
                    'dragon': ['EAFB4', 'F77F8', 'F811A', '10FEEC'],
                    'dragon priest': ['23A93'],
                    'giant': ['23AAE'],
                    'spider': ['FF000E27']
                    }
    for i in range(int(n)):
        object_id = random.choice(object_dict[object_name])
        pyautogui.typewrite(f'~player.placeatme {object_id}\n')
        time.sleep(1.5)

def skyrim_additems(object_name, n):
    object_dict = {
        'gold': 'f',
        'lockpick': 'a'
    }
    object_id = object_dict[object_name]
    pyautogui.typewrite(f'~player.additem {object_id} {int(n)}\n')


def skyrim_souls(n):
    pyautogui.typewrite(f'~player.modav dragonsouls {int(n)}\n')

def skyrim_incskill(skill_name, n):
    for i in range(int(n)):
        pyautogui.typewrite(f'~player.incpcs {skill_name}\n')

while True:
    menu()