from coffee_machine_data import MENU
from coffee_machine_data import resources

profit = 0

def start():
    is_on = True

    show_stats()
    while is_on:
        choice = input("What would you like: espresso (a), latte (b), cappuccino (c)\n").lower()
        if choice == "a":
            print("Espresso")
            cost = MENU['espresso']['cost']
            coins = int(input(f"insert coins - {cost} $ :\n"))
            if coins < cost:
                print("Not enough cash")
            else:
                ingredients = MENU['espresso']['ingredients']
                if change_ressource(ingredients['water'], 0, ingredients['coffee']):
                    print(f"Espresso is coming - chasback is: {coins - cost} $")
        if choice == "b":
            print("Latte")
            cost = MENU['latte']['cost']
            coins = int(input(f"insert coins - {cost} $ :\n"))
            if coins < cost:
                print("Not enough cash")
            else:
                ingredients = MENU['latte']['ingredients']
                if change_ressource(ingredients['water'], ingredients['milk'], ingredients['coffee']):
                    print(f"Latte is coming - chasback is: {coins - cost} $")
        if choice == "c":
            print("Cappuccino")
            cost = MENU['cappuccino']['cost']
            coins = int(input(f"insert coins - {cost} $ :\n"))
            if coins < cost:
                print("Not enough cash")
            else:
                ingredients = MENU['cappuccino']['ingredients']
                if change_ressource(ingredients['water'], ingredients['milk'], ingredients['coffee']):
                    print(f"Cappuccino is coming - chasback is: {coins - cost} $")
        if choice == "report":
            show_stats()
        if choice == "exit":
            is_on = False


def show_stats():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")

def change_ressource(water, milk, coffee):
    if (resources['water'] - water) < 0:
        print("out of water")
        return False
    elif (resources['milk'] - milk) < 0:
        print("out of milk")
        return False
    elif (resources['coffee'] - coffee) < 0:
        print("out of coffee")
        return False
    else:
        resources['water'] -= water
        resources['milk'] -= milk
        resources['coffee'] -= coffee
        return True