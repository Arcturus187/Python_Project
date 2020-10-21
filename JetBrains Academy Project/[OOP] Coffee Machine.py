class CoffeeMachine:
    def __init__(self, water, milk, coffee, cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money
        
    def act_buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        buy_type = input()
        
        if buy_type == 'back':
            self.main_menu()
        
        elif buy_type == '1':
            #250 ml of water and 16 g of coffee beans. It costs $4.
            if self.water >= 250 and self.coffee >= 16 and self.cups >= 1:
                self.water -= 250
                self.coffee -= 16
                self.cups -= 1
                self.money += 4
                print('I have enough resources, making you a coffee!')
            else:
                if self.water < 250:
                    print(f'Sorry, not enough water!') 
                if self.coffee < 16:
                    print(f'Sorry, not enough coffee!') 
                if self.cups < 1:
                    print(f'Sorry, not enough disposable cups!') 
                
        elif buy_type == '2':
            #350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
            if self.water >= 350 and self.milk >= 75 and self.coffee >= 20 and self.cups >= 1:
                self.water -= 350
                self.milk -= 75
                self.coffee -= 20
                self.cups -= 1
                self.money += 7
                print('I have enough resources, making you a coffee!')
            else:
                if self.water < 350:
                    print(f'Sorry, not enough water!') 
                if self.milk < 75:
                    print(f'Sorry, not enough milk!') 
                if self.coffee < 20:
                    print(f'Sorry, not enough coffee!') 
                if self.cups < 1:
                    print(f'Sorry, not enough disposable cups!') 
    
        elif buy_type == '3':
            #200 ml of water, 100 ml of milk, and 12 g of coffee. It costs $6.
            if self.water >= 200 and self.milk >= 100 and self.coffee >= 12 and self.cups >= 1:
                self.water -= 200
                self.milk -= 100
                self.coffee -= 12
                self.cups -= 1
                self.money += 6
                print('I have enough resources, making you a coffee!')
            else:
                if self.water < 200:
                    print(f'Sorry, not enough water!') 
                if self.milk < 100:
                    print(f'Sorry, not enough milk!') 
                if self.coffee < 12:
                    print(f'Sorry, not enough coffee!') 
                if self.cups < 1:    
                    print(f'Sorry, not enough disposable cups!') 
        
    def act_fill(self):
        print('Write how many ml of water do you want to add:')
        self.water += int(input())
        print('Write how many ml of milk do you want to add:')
        self.milk += int(input())
        print('Write how many grams of coffee beans do you want to add:')
        self.coffee += int(input())
        print('Write how many disposable cups of coffee do you want to add:')
        self.cups += int(input())
        
    def act_take(self):
        print(f'I gave you ${self.money}')
        self.money = 0
        
    def act_remaining(self):
        print(f'''The coffee machine has:
        {self.water} of water
        {self.milk} of milk
        {self.coffee} of coffee beans
        {self.cups} of disposable cups
        {self.money} of money
        ''')
        
    def main_menu(self):
        print()
        while True:
            print('Write action (buy, fill, take, remaining, exit):')
            menu = input()
        
            if menu == 'buy':
                self.act_buy()
            if menu == 'fill':
                self.act_fill()
            if menu == 'take':
                self.act_take()
            if menu == 'remaining':
                self.act_remaining()
            if menu == 'exit':
                exit()
        
my_coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
my_coffee_machine.main_menu()
