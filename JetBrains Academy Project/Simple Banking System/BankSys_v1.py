import random


class BankSys:
    # id: {'pin': ,'balance':}
    account_data = {}

    def main_menu(self):
        print('''1. Create an account
2. Log into account
0. Exit''')

        menu_num = input()
        print()
        if menu_num == '1':
            self.create_account()
        elif menu_num == '2':
            self.login()
        elif menu_num == '3':
            self.quit()
        else:
            print('Invalid input')
            self.main_menu()

    def quit(self):
        print('Bye!')
        exit()

    def create_account(self):
        # Create Random card number
        tmp_list = []
        for i in range(10):
            tmp_list.append(str(random.randint(0, 9)))
        tmp_list = ''.join(tmp_list)
        card_num = f"400000{tmp_list}"
        # Create PIN
        pin = []
        for i in range(4):
            pin.append(str(random.randint(0, 9)))
        pin = ''.join(pin)
        # Store data in dict
        self.account_data[card_num] = {'pin': pin, 'balance': 0}
        #print(self.account_data)

        # Output
        print(f'''Your card has been created
Your card number:
{card_num}
Your card PIN:
{pin}''')
        print()

        self.main_menu()

    def login(self):
        print('Enter your card number:')
        card_num = input()
        print('Enter your PIN:')
        pin = input()
        print()

        # Check Condition
        if card_num not in self.account_data.keys():
            print('Wrong card number or PIN!')
            print()
            self.main_menu()
        elif self.account_data[card_num]['pin'] == pin:
            print('You have successfully logged in!')
            print()
            self.log_menu(card_num)
        else:
            print('Wrong card number or PIN!')
            print()
            self.main_menu()

    def log_menu(self, card_num):
        print('''1. Balance
2. Log out
0. Exit''')
        menu_num = input()
        print()

        if menu_num == '1':
            self.balance(card_num)
        elif menu_num == '2':
            self.main_menu()
        elif menu_num == '3':
            self.quit()
        else:
            print('Invalid input')
            self.log_menu(card_num)

    def balance(self, card_num):
        print(f'Balance: {self.account_data[card_num]["balance"]}')
        print()
        self.log_menu(card_num)


bni = BankSys()
bni.main_menu()
