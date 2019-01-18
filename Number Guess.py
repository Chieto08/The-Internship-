import random

random_number = random.randint(1, 100)
number_of_guesses = 0
guessed_number = 0
while guessed_number != random_number:
    guessed_number = int(input("Make a guess from 1-100: "))
    number_of_guesses = number_of_guesses + 1
    if guessed_number < random_number:
        print("Number is lower than correct number, guess again.")
    elif guessed_number > random_number:
        print("Number is greater than correct number, guess again.")
    else:
        print("Correct guess!, Number of guesses is: " + str(number_of_guesses)
              )
        break
