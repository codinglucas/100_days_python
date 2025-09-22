# both computer and user take two cards
# both them are asked if they want to get another one or not

import random

cards = {"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9,"10": 10,"J": 10, "K": 10,"Q": 10}

def get_initial_cards(num, user_choice, sum, cards_list):
    if user_choice != "y":
        sum = 0
        cards_list = ""
        for c in range(num):
            card_selected = str(random.choice(list(cards.keys())))
            sum += cards[card_selected]

            cards_list += card_selected + " "
    else:
        for c in range(num):
            card_selected = str(random.choice(list(cards.keys())))
            sum += cards[card_selected]

            cards_list += card_selected + " "

    return sum, cards_list

def compare_scores(user_sum, computer_sum):
    if user_sum > 21:
        return "You lost!"
    elif computer_sum > 21:
        return "Computer went over"
    elif user_sum == 21:
        return "Win with a Blackjack!"
    elif computer_sum == 21:
        return "Lost! Opponent has a Blackjack"
    elif user_sum == computer_sum:
        return "Draw"
    elif user_sum > computer_sum:
        return "You lost!"
    else:
        return "You win"

while True:
    print(" --- STARTING GAME --- ")
    user_sum, user_cards_list = get_initial_cards(2, "start", 0, "")
    print("Your cards: ", user_cards_list, "\n", "Sum: ", user_sum)

    computer_sum, computer_cards_list = get_initial_cards(2, "start", 0, "")
    print("Computer cards: ", computer_cards_list, "\n", "Sum: ", computer_sum)



    user_choice = input("Take another card? 'y' for yes, 'n' for no ").lower()
    computer_choice = random.randint(0,1)



    if user_choice == "y":
        user_sum, user_cards_list = get_initial_cards(1, user_choice, user_sum, user_cards_list)
        #print("Your cards: ", cards_list, "\n", "Sum: ", user_sum)

    if computer_choice == 1:
        computer_sum, computer_cards_list = get_initial_cards(1, "y", computer_sum, computer_cards_list)
        #print("Computer cards: ", computer_cards_list, "\n", "Sum: ", computer_sum)

    print(" --- NEW ROUND ---")
    
    print("Your cards: ", user_cards_list, "\n", "Sum: ", user_sum)
    print("Computer cards: ", computer_cards_list, "\n", "Sum: ", computer_sum, "\n", "Computer choice: ", computer_choice)

    print(compare_scores(user_sum, computer_sum))

    keep = input("Continue? ")
    if keep == "y":
        continue
    else:
        break
