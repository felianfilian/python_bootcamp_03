import random

from high_low_data import data

def start():
    game_running = True
    score = 0
    while game_running:
        quest01 = random.choice(data)
        while True:
            quest02 = random.choice(data)
            if quest01['name'] != quest02['name']:
                break

        a_name = quest01['name']
        b_name = quest02['name']
        a_follower = quest01['follower_count']
        b_follower = quest02['follower_count']

        print(f"\nScore = {score}")
        print("Who has more follower?")
        guess = input(f"{a_name} (a) VS {b_name} (b) - end game (c)\n").lower()

        if guess == "a" and a_follower > b_follower:
            print("You are right")
            score += 1
        elif guess == "b"  and b_follower > a_follower:
            print("You are right")
            score += 1
        elif guess == "c":
            game_running = False
        else:
            print("That is wrong")
        print(f"{a_name} = {a_follower}")
        print(f"{b_name} = {b_follower}")