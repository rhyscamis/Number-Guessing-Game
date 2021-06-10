import random

random_number = random.randint(1, 30)
print("Guess a number from 1 to 30, you have 5 attempts")

attempts = 0

while attempts < 5:
    guess = int(input("Guess a number: "))
    attempts += 1
    if guess == random_number:
        print("You have guessed correctly!")
        break
    if guess > random_number:
        print("Your guess was too high!")
    elif guess < random_number:
        print("Your guess was too low!")
    
    if attempts == 5:
        print("You have run out of guesses, the number was " + str(random_number))