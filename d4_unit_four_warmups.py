age = int(input("How old are you?"))

if age <= 2 and age >= 0:
    print("You got a free ticket")
elif age >= 13:
    print("The ticket is 10 dollars")
elif age >= 3 and age <= 12:
    print("The ticket is 8 dollars")
elif age <= 0:
    print("This is not a valid age, don't fool me")