# coffe machine project : 

from menu import *
profit = 0


# is transition successfuly :
def is_transaction_succesful(money_received, drink_cost):
    """return true when the payment is accepted, or fales if the money is insufficient."""
    if money_received >= drink_cost:
        global profit
        profit += drink_cost
        return True
    
    else : 
        print('Sorry thats not enough money, money refunded.')
        return False



# coin enter : 
def process_coin():
    print('Please insert coins.')
    total = int(input('how many quarters? : ')) * 0.25
    total += int(input('how many dimes?: ')) * 0.1
    total += int(input('how many nickles: ')) * 0.05
    total += int(input('how many pennies?:')) * 0.01

    return total


# Create a function to hundle the ressource sufficient : 
def is_en_ressource(order_ingredient):
    is_enough = True
    for item in order_ingredient:
        if order_ingredient[item] >= ressource[item]:
            print('sorry there is not enough water.')
            return is_enough
    return is_enough

while True:
    choice_input = input('what would you like? (espresso/latte/cappuccino):')
    if choice_input == 'off':
        break
    elif choice_input == 'report':
        print(f"Water: {ressource['water']}ml")
        print(f"Milk: {ressource['milk']}ml")
        print(f"Coffee: {ressource['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice_input]
        if(is_en_ressource(drink)):
            # There enough ressource :
            process = process_coin()
            if process == drink['cost']:
                pass