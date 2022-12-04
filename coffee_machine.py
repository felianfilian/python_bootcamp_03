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
                if check_ressource(ingredients):
                    change_ressource(ingredients)
                    print(f"Espresso is coming - chasback is: {coins - cost} $")
        if choice == "b":
            print("Latte")
            cost = MENU['latte']['cost']
            coins = int(input(f"insert coins - {cost} $ :\n"))
            if coins < cost:
                print("Not enough cash")
            else:
                ingredients = MENU['latte']['ingredients']
                if check_ressource(ingredients):
                    change_ressource(ingredients)
                    print(f"Latte is coming - chasback is: {coins - cost} $")
        if choice == "c":
            print("Cappuccino")
            cost = MENU['cappuccino']['cost']
            coins = int(input(f"insert coins - {cost} $ :\n"))
            if coins < cost:
                print("Not enough cash")
            else:
                ingredients = MENU['cappuccino']['ingredients']
                if check_ressource(ingredients):
                    change_ressource(ingredients)
                    print(f"Cappuccino is coming - chasback is: {coins - cost} $")
        if choice == "report":
            show_stats()
        if choice == "exit":
            is_on = False


def show_stats():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")


def check_ressource(ingredients):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"there is not enough {item}")
            return False
    return True

def change_ressource(ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
