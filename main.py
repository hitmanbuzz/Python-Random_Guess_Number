import random

guess = int(input("Enter a number: "))

guess_number = random.randint(0, 10)
while guess != guess_number:
    guess = int(input("Enter a number: "))
if guess == guess_number:
    print("You have won")