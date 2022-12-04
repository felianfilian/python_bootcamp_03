import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_next = True

def get_card():
    """return random card from deck"""
    return random.choice(cards)

def get_sum(list):
    if 11 in list and sum(list) > 21:
        list.remove(11)
        list.append(1)
    return sum(list)

def dealer_ai(sum):
    if sum <= 16:
        return True
    else:
        return False

def wincheck(dealer_sum, player_sum):
    if dealer_sum == 21:
        print("Dealer Wins")
    elif dealer_sum > 21:
        print("Dealer Loose")
    elif player_sum > 21:
        print("Player Loose")
    elif dealer_sum > player_sum:
        print("Dealer Wins")
    elif dealer_sum < player_sum:
        print("Player Wins")
    elif dealer_sum == player_sum:
        print("DRAW")

def start():
    dealer_cards = []
    player_cards = []
    game_running = True
    dealer_sum = 0

    # first round
    player_cards.append(get_card())
    dealer_cards.append(get_card())
    print(f"Dealer: {dealer_cards}")

    while game_running:
        # next card
        player_cards.append(get_card())
        if dealer_sum <= 16:
            dealer_cards.append(get_card())
        # get sums
        dealer_sum = get_sum(dealer_cards)
        player_sum = get_sum(player_cards)

        # print stats
        print(f"Player: {player_cards} = {player_sum}")
        if dealer_sum == 21 or player_sum == 21 or dealer_sum > 21 or player_sum > 21 or input("next card? (y/n)\n") == "n":
            while dealer_sum <= 16:
                dealer_cards.append(get_card())
                dealer_sum = get_sum(dealer_cards)
            game_running = False
            print("\nGame finished")
            print(f"Dealer: {dealer_cards} = {dealer_sum}")
            print(f"Player: {player_cards} = {player_sum}")
            wincheck(dealer_sum, player_sum)




