from high_low_data import data

def start():
    guess = input(f"{data[0]['name']} (a) VS {data[1]['name']} (b)\n")
    if guess == "a":
        print("a")
    elif guess == "b":
        print("b")
    else:
        print("wrong input")