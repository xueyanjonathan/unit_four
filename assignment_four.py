import random

def getCard():
    card = random.randint(1,10)
    return card

def getUserTotal():
    user_total = getCard() + getCard()
    print("Your total is ", user_total)
    draw_a_card = input("Would you like to hit or stay?")
    if draw_a_card == "hit":
        user_total = user_total + getCard()
        print("Your total is now", user_total)
    return user_total

def getDealerTotal():
    dealer_total = getCard() + getCard()
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

