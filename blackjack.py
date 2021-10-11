import os
import random 


def first_cards(cards):
    """Takes the deck as argument, creates an empty list, adds the 2 first cards and returns the list """
    pair_of_cards = []
    for i in range(2):
        card = random.choice(list(cards.keys()))
        pair_of_cards.append(card)
    return pair_of_cards

def score_calculator(cards, cards_list):
    """Takes as arguments the deck and the corresponding cards of the computer/user.
    Then calculates the total value of the cars and returns it."""
    sum = 0 
    for i in range(len(cards_list)):
        # e.g if i=0 and cards_list[0]='J' then cards['J'][0]=10
        sum += cards[cards_list[i]][0]
    # Check if an Ace exists and if the sum is over 21 in order to the change the value of 'A' from 11 to 1.
    if 'A' in cards_list and sum > 21:
        # Use count() in case an Ace exists more than 1 time.
        sum = sum - (cards_list.count("A") * 10)
    return sum

def is_blackjack(c_cards, c_score, u_cards, u_score):
    """Takes as arguments the first pair of cards for both the computer and the user, and their scores.
    Then checks if there is a blackjack by hand."""
    if c_score == 21:
        print(f" {c_cards} -> Computer score is {c_score}.  BLACKJACK! COMPUTER WINS!")
    elif u_score == 21:
        print(f" {u_cards} -> Your score is {u_score}.  BLACKJACK! YOU WIN!")

def card_exists(cards, cards_list):
    """Takes as arguments the deck and the cards that the user/computer has in their hands in the given moment.
    Then picks a random card from the deck. If all of the 4 cards in the deck that represent this card have already been handed it picks another one.
    Then it appends the card in the list of cards."""
    while True:
        card = random.choice(list(cards.keys()))
        # e.g cards['2'][1] = 4, that goes for every card in the begining of the game.
        if cards[card][1] > 0:
            cards_list.append(card)
            cards[card][1] = cards[card][1] - 1
            break
        else:
            continue


if __name__ == '__main__':

    # This loop repeats if the user wants to play again after the game is over.
    while True:
        # This dictionary reprents the deck. Keys are the cards, values are lists. 1st element of the list is the value of the card, 2nd is how many cards exist in the deck.
        cards = {
        '2': [2, 4], '3': [3, 4], '4': [4, 4], '5': [5, 4], '6': [6, 4], '7': [7, 4], '8':[8, 4], '9': [9, 4], '10':  [10, 4], 'J': [10, 4], 'Q': [10, 4], 'K': [10, 4], 'A': [11, 4]
        }
        # Generating the first pair for cards.
        computer_cards = first_cards(cards)
        user_cards = first_cards(cards)
        # Calculating the score of each pair.
        user_score = score_calculator(cards, user_cards)
        computer_score = score_calculator(cards, computer_cards)
        # Checking if there is a blackjack.
        is_blackjack(computer_cards, computer_score, user_cards, user_score)
        # This loop repeats until (1) the user does not want another card and (2) user score is not 21 and (3) user score is not over 21.
        # Also it is overriden when there is a blackjack.
        while True and user_score != 21 and computer_score != 21:
            print(f"Computer cards -> ['{computer_cards[0]}', X]")
            print(f"{user_cards} -> Your score is {user_score}. ")
            another_card = input("Do yo want another card? Type 'yes or 'no': ")
            if another_card == 'yes':
                card_exists(cards, user_cards)
                user_score = score_calculator(cards, user_cards)
            elif another_card != 'no':
                print(f"{another_card} is not an available option. Check for typos.  ")
            # Checking if with the new given card the user hits 21 or goes over it.
            if user_score == 21:
                print(f"{user_cards} -> Your score is {user_score}. YOU WIN!  ")
                break
            elif user_score > 21:
                print(f"{user_cards} -> Your score is {user_score}. YOU LOSE!  ")
                break
            elif another_card == 'no':
                break
        # This loop repeats until (1) computer score is not over 16 and (2) user score in not greater or equal to 21.
        while computer_score <= 16 and user_score < 21:
            print("Computer takes one card.  ")
            card_exists(cards, computer_cards)
            computer_score = score_calculator(cards, computer_cards)
            print(f"{computer_cards} -> Computer score is {computer_score}.  ")
        # Checking who wins, if the user score is not greater or equal to 21 already.
        if user_score < 21:
            if computer_score > 21:
                print("YOU WIN!  ")
            elif user_score > computer_score:
                print(f"{user_cards} -> Your score is {user_score}.  YOU WIN!  ")
            elif user_score == computer_score:
                print(f"{user_cards} -> Your score is {user_score}.  DRAW!  ")
            else:
                print(f"{user_cards} -> Your score is {user_score}.  YOU LOSE!  ")

    
        play_again = input("Type any key to play again or 'q' to exit: ")
        if play_again == 'q':
            exit()
        else:
            os.system('cls')
        

    

    
        








