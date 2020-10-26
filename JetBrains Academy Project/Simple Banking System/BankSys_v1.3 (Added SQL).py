import random
import sqlite3

main_menu = '''1. Create an account
2. Log into account
0. Exit'''

login_menu = '''1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit'''

CREATE_TABLE = '''CREATE TABLE IF NOT EXISTS card ('id' INTEGER, number TEXT, pin TEXT, balance INTEGER); '''

INSERT_NEW_CARD = 'INSERT INTO card (number, pin, balance) VALUES (?, ?, ?);'

FETCH_ALL_CLIENT = 'SELECT number FROM card'
FETCH_DATA_BY_ID = 'SELECT pin, balance FROM card WHERE number = ?'

CHANGE_BALANCE_BY_ID = 'UPDATE card SET balance = ? WHERE number = ?'
DELETE_ACCOUNT_BY_ID = 'DELETE FROM card WHERE number = ?'

connection = sqlite3.connect('card.s3db')

with connection:
    connection.execute(CREATE_TABLE)

def delete_account_by_id(card_num):
    connection.execute(DELETE_ACCOUNT_BY_ID, (card_num,))
    connection.commit()

def change_balance_by_id(card_num, updated_balance):
    connection.execute(CHANGE_BALANCE_BY_ID, (updated_balance, card_num))
    connection.commit()

def insert_new_card(card_num, pin, balance):
    connection.execute(INSERT_NEW_CARD, (card_num, pin, balance))
    connection.commit()

def fetch_card_data(card_num):
    return connection.execute(FETCH_DATA_BY_ID, (card_num,)).fetchone()

def fetch_all_client():
    return connection.execute(FETCH_ALL_CLIENT).fetchall()

class BankSys:
    def main_menu(self):
        print(main_menu)
        menu_num = input()
        print()
        if menu_num == '1':
            self.create_account()
        elif menu_num == '2':
            self.login()
        elif menu_num == '0':
            self.quit()
        else:
            print('Invalid input')
            self.main_menu()

    def quit(self):
        print('Bye!')
        connection.close()
        exit()

    def create_account(self):
        def checksum(num):
            num = [int(x) for x in num]
            del_num = []
            app_num = []
            for x in num[::-2]:
                del_num.append(x)
                app_num.append((x * 2))
            for i in del_num:
                num.remove(i)
            for i in app_num:
                if i > 9:
                    num.append(i - 9)
                else:
                    num.append(i)
            del del_num
            checksum_digit = str((10 - (sum(num) % 10)) % 10)
            return checksum_digit

        # Create Random card number
        tmp_list = []
        for i in range(9):
            tmp_list.append(str(random.randint(0, 9)))
        tmp_list = ''.join(tmp_list)
        card_num = f"400000{tmp_list}"  # No Checksum Digit
        card_num = card_num + checksum(card_num)


        # Create PIN
        pin = []
        for i in range(4):
            pin.append(str(random.randint(0, 9)))
        pin = ''.join(pin)
        # Store data in database
        insert_new_card(card_num, pin, 0)
        # Output
        print(f'''Your card has been created
Your card number:
{card_num}
Your card PIN:
{pin}''')
        print()

        self.main_menu()

    def login(self):
        def log_menu(card_num):
            def balance(card_num):
                this_card = fetch_card_data(card_num)
                balance = this_card[1]
                print(f'Balance: {balance}')
                print()
                log_menu(card_num)

            def add_income(card_num):
                print('Enter income:')
                income = input()
                if not income.isdecimal():
                    print('invalid input, try again!')
                    print()
                    log_menu(card_num)
                else:
                    income = int(income)
                    this_card = fetch_card_data(card_num)
                    new_balance = int(this_card[1]) + income
                    change_balance_by_id(card_num, str(new_balance))
                    print('Income was added!')
                    print()
                    log_menu(card_num)

            def do_transfer(card_num):
                def checksum(num):
                    num = [int(x) for x in num]
                    del_num = []
                    app_num = []
                    for x in num[::-2]:
                        del_num.append(x)
                        app_num.append((x * 2))
                    for i in del_num:
                        num.remove(i)
                    for i in app_num:
                        if i > 9:
                            num.append(i - 9)
                        else:
                            num.append(i)
                    del del_num
                    checksum_digit = str((10 - (sum(num) % 10)) % 10)
                    return checksum_digit
                print('Transfer')
                print('Enter card number:')
                transfer_card_num = input()

                if len(transfer_card_num) != 16 or not transfer_card_num.isdecimal():
                    print('Probably you made a mistake in the card number. Please try again!')
                    print()
                    log_menu(card_num)
                elif checksum(transfer_card_num[:15]) != transfer_card_num[15]:
                    print('Probably you made a mistake in the card number. Please try again!')
                    print()
                    log_menu(card_num)
                elif transfer_card_num == card_num:
                    print("You can't transfer money to the same account!")
                    print()
                    log_menu(card_num)
                elif (transfer_card_num,) not in fetch_all_client():
                    print('Such a card does not exist.')
                    print()
                    log_menu(card_num)
                else:
                    print('Enter how much money you want to transfer:')
                    transfer_money = input()
                    if not transfer_money.isdecimal():
                        print('Invalid input, try again!')
                        print()
                        log_menu(card_num)
                    else:
                        transfer_money = int(transfer_money)
                        card_data = fetch_card_data(card_num)
                        if transfer_money > card_data[1]:
                            print('Not enough money!')
                            print()
                            log_menu(card_num)
                        else:
                            transfer_card_data = fetch_card_data(transfer_card_num)
                            substract_amount = card_data[1] - transfer_money
                            addition_amount = transfer_card_data[1] + transfer_money
                            change_balance_by_id(card_num, substract_amount)
                            change_balance_by_id(transfer_card_num, addition_amount)
                            print('Success!')
                            print()
                            log_menu(card_num)

            def close_account(card_num):
                delete_account_by_id(card_num)
                print('The account has been closed!')
                print()
                self.main_menu()

            print(login_menu)
            menu_num = input()
            print()

            if menu_num == '1':
                balance(card_num)
            elif menu_num == '2':
                add_income(card_num)
            elif menu_num == '3':
                do_transfer(card_num)
            elif menu_num == '4':
                close_account(card_num)
            elif menu_num == '5':
                self.main_menu()
            elif menu_num == '0':
                self.quit()
            else:
                print('Invalid input')
                log_menu(card_num)


        print('Enter your card number:')
        card_num = input()
        print('Enter your PIN:')
        pin = input()
        print()

        # Check Condition
        if (card_num,) not in fetch_all_client():
            print('Wrong card number or PIN!')
            print()
            self.main_menu()
        elif (card_num,) in fetch_all_client():
            data = fetch_card_data(card_num)
            if data[0] == pin:
                print('You have successfully logged in!')
                print()
                log_menu(card_num)
            else:
                print('Wrong card number or PIN!')
                print()
                self.main_menu()

bni = BankSys()
bni.main_menu()
connection.close()