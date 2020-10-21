def stock_list():
    print(f'''The coffee machine has:
    {water_stock} of water
    {milk_stock} of milk
    {coffee_stock} of coffee beans
    {cups_stock} of disposable cups
    {money_stock} of money
    ''')
    
def action_buy():
    global water_stock, milk_stock, coffee_stock, cups_stock, money_stock
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
    buy_type = input()
    
    if buy_type == 'back':
        main_menu()
    
    elif buy_type == '1':
        #250 ml of water and 16 g of coffee beans. It costs $4.
        if water_stock >= 250 and coffee_stock >= 16 and cups_stock >= 1:
            water_stock -= 250
            coffee_stock -= 16
            cups_stock -= 1
            money_stock += 4
            print('I have enough resources, making you a coffee!')
        else:
            if water_stock < 250:
                print(f'Sorry, not enough water!') 
            if coffee_stock < 16:
                print(f'Sorry, not enough coffee!') 
            if cups_stock < 1:
                print(f'Sorry, not enough disposable cups!') 
            
    elif buy_type == '2':
        #350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
        if water_stock >= 350 and milk_stock >= 75 and coffee_stock >= 20 and cups_stock >= 1:
            water_stock -= 350
            milk_stock -= 75
            coffee_stock -= 20
            cups_stock -= 1
            money_stock += 7
            print('I have enough resources, making you a coffee!')
        else:
            if water_stock < 350:
                print(f'Sorry, not enough water!') 
            if milk_stock < 75:
                print(f'Sorry, not enough milk!') 
            if coffee_stock < 20:
                print(f'Sorry, not enough coffee!') 
            if cups_stock < 1:
                print(f'Sorry, not enough disposable cups!') 
  
    elif buy_type == '3':
        #200 ml of water, 100 ml of milk, and 12 g of coffee. It costs $6.
        if water_stock >= 200 and milk_stock >= 100 and coffee_stock >= 12 and cups_stock >= 1:
            water_stock -= 200
            milk_stock -= 100
            coffee_stock -= 12
            cups_stock -= 1
            money_stock += 6
            print('I have enough resources, making you a coffee!')
        else:
            if water_stock < 200:
                print(f'Sorry, not enough water!') 
            if milk_stock < 100:
                print(f'Sorry, not enough milk!') 
            if coffee_stock < 12:
                print(f'Sorry, not enough coffee!') 
            if cups_stock < 1:    
                print(f'Sorry, not enough disposable cups!') 
        
def action_fill():
    global water_stock, milk_stock, coffee_stock, cups_stock
    print('Write how many ml of water do you want to add:')
    water_stock += int(input())
    print('Write how many ml of milk do you want to add:')
    milk_stock += int(input())
    print('Write how many grams of coffee beans do you want to add:')
    coffee_stock += int(input())
    print('Write how many disposable cups of coffee do you want to add:')
    cups_stock += int(input())
    
def action_take():
    global money_stock
    print(f'I gave you ${money_stock}')
    money_stock = 0
    
def main_menu():
    print()
    while True:
        print('Write action (buy, fill, take, remaining, exit):')
        menu = input()
    
        if menu == 'buy':
            action_buy()
        if menu == 'fill':
            action_fill()
        if menu == 'take':
            action_take()
        if menu == 'remaining':
            stock_list()
        if menu == 'exit':
            exit()
        
        
# Starting Stock: $550, 400 ml of water, 540 ml of milk, 120 g of coffee beans, and 9 disposable cups.
water_stock = 400
milk_stock = 540
coffee_stock = 120
cups_stock = 9
money_stock = 550

main_menu()
