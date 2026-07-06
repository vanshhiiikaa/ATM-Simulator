import random
number = random.randint(1, 100)
while True:
 for i in range(1, 6):
    print("Attempt", i)
    if i == 5:
        print("You have used all your attempts. The number was", number)
        break
    x = (input("Welcome to the Number Guessing Game! Think of a number between 1 and 100, and I will try to guess it: "))
    if number == int(x):
        print("You guessed my number! It is", number)
        break
    elif number < int(x):
        print("Think of a lower number")
    else:
        print("Think of a higher number")