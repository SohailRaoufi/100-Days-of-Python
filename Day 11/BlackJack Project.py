from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
user_card = []
computer_card = []
user_value = 0
computer_value = 0


def deal_card():
    if user_card == [] and computer_card == []:
        for i in range(2):
            user_card.append(random.choice(cards))
            computer_card.append(random.choice(cards))
    else:
        user_card.append(random.choice(cards))
        computer_card.append(random.choice(cards))


def blackjack():
    if user_value > 21 and computer_value > 21:
        print("Draw")
    elif user_value > 21:
        print("you Lose!")
    elif computer_value > 21:
        print("You Won")
    elif user_value == computer_value:
        print("Draw")
    elif computer_value > user_value:
        print("You Lose")
    elif user_value > computer_value:
        print("you Won")


ask_to_play = input("Do you want to play BlackJack Game?[Y/N]\n").lower()
if ask_to_play == 'y':
    deal_card()
    print(logo)

    user_value = sum(user_card)
    computer_value = sum(computer_card)

    print(f'Your Cards {user_card}.')
    print(f'Computer First Card {computer_card[0]}')

    if user_value == 21:
        print("You Won")
    elif computer_value == 21:
        print("You Lose!")
    else:
        ask_for_card = input(
            "Do you want to pick another card?[Y/N]\n").lower()
        if ask_for_card == 'y':
            deal_card()
            user_value = sum(user_card)
            computer_value = sum(computer_card)
            blackjack()
        elif ask_for_card == 'n':
            if computer_value < 16:
                computer_card.append(random.choice(cards))
                computer_value = sum(computer_card)
                blackjack()
