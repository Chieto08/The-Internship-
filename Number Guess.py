import random

random_number = random.randint(1, 100)
guessed_number = 0
guessed_numbers = []
while guessed_number != random_number:
    guessed_number = int(input("Make a guess from 1-100: "))
    if guessed_number not in guessed_numbers:
        guessed_numbers.append(guessed_number)
    if guessed_number < random_number:
        print("Number is lower than correct number, guess again.")
    elif guessed_number > random_number:
        print("Number is greater than correct number, guess again.")
    else:
        print("Correct guess!, Number of guesses is: " + str(len(guessed_numbers))
              )
        break
