from menu_data import MENU , resources

MONEY = 0

def print_report():
    """This Function Print the resoureces and amount in machine"""
    for resource in resources:
        if resource == 'water' or resource == 'milk':
            print(f'{resource}: {resources[resource]} ml')
        else:
            print(f'{resource}: {resources[resource]} g')
    print(f'Money: ${MONEY}')

def check_resources(user_input):
    """This Function checks that resources are enough to make the coffee or not"""
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    if user_input == 'espresso':
        if water > MENU['espresso']['ingredients']['water'] and coffee > MENU['espresso']['ingredients']['coffee']:
            return True
        else:
            return False
    elif user_input == 'latte':
        if water > MENU['latte']['ingredients']['water'] and coffee > MENU['latte']['ingredients']['coffee'] and milk > MENU['latte']['ingredients']['milk']:
            return True
        else:
            return False
    elif user_input == 'cappuccino':
        if water > MENU['cappuccino']['ingredients']['water'] and coffee > MENU['cappuccino']['ingredients']['coffee'] and milk > MENU['latte']['ingredients']['milk']:
            return True
        else:
            return False
def process_coins(quarter , dimes , nickles , pennies , user_input):
    """This Function takes quarter , dimes , nickles , pennies and user input and calculate the coing in dolor and check it match the coffe amount or not"""
    #quarter = 0.25 , dimes = 0.10 , nickles = 0.05 , pennies = 0.01
    calculate_money = (0.25 * quarter) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    cost = MENU[user_input]['cost']
    if cost == calculate_money:
        return 'Here is Your Coffee!! Enjoy'
    elif calculate_money > cost:
        reamin_money = round(calculate_money - cost , 2)
        return f'Here is Your Exchange ${reamin_money}\nHere is your Coffee!! Enjoy'
    else:
        return 'Sorry That is not enough Money!! Money Refunded.'

#Main
while True:
    user_input = input("What Would You Like ? (espresso , latte , cappuccino)\n")
    if user_input == 'off':
        break
    elif user_input == 'report':
        print_report()
    else:
        resource = check_resources(user_input)
        if resource:
            quarter = float(input('coin in quarter: '))
            dimes = float(input('coin in dimes: '))
            nickles = float(input('coin in nikcles: '))
            pennies = float(input('coin in pennies: '))
            res = process_coins(quarter , dimes , nickles , pennies , user_input)
            print(res)
            if res != 'Sorry That is not enough Money!! Money Refunded.':
                cost = MENU[user_input]['cost']
                MONEY += cost
                water = MENU[user_input]['ingredients']['water']
                coffee = MENU[user_input]['ingredients']['coffee']
                if user_input == 'latte' or user_input == 'cappuccino':
                    milk = MENU[user_input]['ingredients']['milk']
                    resources['water'] -= water
                    resources['coffee'] -= coffee
                    resources['milk'] -= milk
                else:
                    resources['water'] -= water
                    resources['coffee'] -= coffee
        else:
            print("Not Enough Resources!!!")




