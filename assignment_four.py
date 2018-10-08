# Jonathan Lin
# 10/08/2018
# if, else, and elif
# Using if type commands to write functions to create a simplified version of Black Jack


import random


def getCard():
    """
    This function randomly selects a card number between 1 and 10, and returns the card number.
    :return: card number
    """
    card = random.randint(1, 10)
    return card


def getUserTotal():
    """
    This function allows the user to draw two cards, and helps the user calculate the total.
    It prints the result to the user
    The user has the choice to hit or stay.
    If the user hits, the function draws one more card and adds the number to the user's total.
    If the user stays, the function would not draw a card.
    The function returns the user's total.
    :return: The user's total from the cards drawn
    """
    card_one = getCard()
    card_two = getCard()
    card_three = getCard()
    user_total = card_one + card_two
    print("You drew a", card_one, "and a", card_two)
    print("Your total is ", user_total)
    draw_a_card = input("Would you like to hit or stay?")
    if draw_a_card == "hit":
        print("You drew a", card_three)
        user_total = user_total + card_three
        print("Your total is now", user_total)
    return user_total


def getDealerTotal():
    """
    The function lets the dealer draw two cards and helps the user calculate the dealer's total.
    It prints the result to the user.
    The function returns the dealer's total.
    :return: The dealer's total from the cards drawn
    """
    dealer_card_one = getCard()
    dealer_card_two = getCard()
    dealer_total = dealer_card_one + dealer_card_two
    print("The dealer has a", dealer_card_one, "and a", dealer_card_two)
    print("The dealer total is", dealer_total)
    return dealer_total


def main():
    userNumber = getUserTotal()
    if userNumber >= 21:
        print("You lose")
    else:
        dealerNumber = getDealerTotal()
        if userNumber >= dealerNumber:
            print("You win")
        else:
            print("You lose")


main()
