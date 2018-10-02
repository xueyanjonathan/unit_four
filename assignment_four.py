import random

def getUserTotal():
    user_first_total = random.randint(1, 10) + random.randint(1, 10)
    print("Your total is ", user_first_total)
    draw_a_card = input("Do you want to draw another card?")



def main():
    userNumber = getUserTotal
    dealerNumber = getDealerTotal
    if userNumber => dealerNumber:
        print("Congratulations, you win!")
    if userNumber =< dealerNumber:
        print("You lose.")