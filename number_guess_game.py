import random

print("Hi welcome to the game, This is a number guessing game.\nYou got 7 chances to guess the number. Let's start the game")


number_to_be_guessed = random.randint(0,100)

total_no_of_guesses = 7

no_of_guesses = 0

while no_of_guesses < total_no_of_guesses:

    no_of_guesses += 1

    choosen_number = int(input(f"Guess the number between 0 and 100 : "))

    if choosen_number == number_to_be_guessed:
        print(f"congratulations you guesses correct one , its {number_to_be_guessed} in just {no_of_guesses}")
        break
    elif no_of_guesses == 7 and number_to_be_guessed != choosen_number:
        print("oops you done with your chances \n come back tomorrow")
    elif choosen_number < number_to_be_guessed:
        print("your guess is too low \n Try Again !!!",f"You have {total_no_of_guesses - no_of_guesses} left to guess ") 
    elif choosen_number > number_to_be_guessed:
        print("your guess is too high \n Try Again !!!",f"You have {total_no_of_guesses - no_of_guesses} left to guess ") 
    else:
        print("Error occured ")    
