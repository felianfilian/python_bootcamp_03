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

        print(f"\nScore = {score}")
        print("Who has more follower?")
        guess = input(f"{quest01['name']} (a) VS {quest02['name']} (b) - end game (c)\n")

        if guess == "a" and quest01['follower_count'] > quest02['follower_count']:
            print("You are right")
            score += 1
        elif guess == "b"  and quest02['follower_count'] > quest01['follower_count']:
            print("You are right")
            score += 1
        elif guess == "c":
            game_running = False
        else:
            print("That is wrong")
        print(f"{quest01['name']} = {quest01['follower_count']}")
        print(f"{quest02['name']} = {quest02['follower_count']}")