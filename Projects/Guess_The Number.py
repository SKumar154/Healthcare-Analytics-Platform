import random

print("Welcome! To the Guessing Game \nYou have 7 chances to guess the number Let's start!")

low = int(input("What is the Lower bound? "))
high = int(input("What is the Upper bound? "))

print(f"You have 7 chances to guess the number between {low} (inclusive) and {high} (inclusive)")

num = random.randint(low, high)

chances = 7
current = 0

while (current < chances):

    current += 1
    guess = int(input("Enter your guess: "))

    if(guess == num):
        print(f"Bravo! You guess the number {num} correctly in {current} attempts.")
        break
    elif(guess != num and current > chances):
        print(f"Nice try! But your chances to guess are up. The number was {num}")
    elif(guess > num):
        print("The number is lower than this.")
    elif(guess < num):
        print("The number is higher than this.")
