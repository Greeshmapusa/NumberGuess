import random
import time

# Pick a random number between 1 and 200
secret_number = random.randint(1, 200)

def welcome():
    print("What's your name?")
    player_name = input()
    print(f"Hello, {player_name}! Let's play a guessing game. I have a number between 1 and 200.")
    time.sleep(0.5)
    print("Try to guess it!")

def guess_game():
    attempts = 0
    while attempts < 6:
        time.sleep(0.25)
        user_input = input("Your guess: ")
        try:
            user_guess = int(user_input)

            if 1 <= user_guess <= 200:
                attempts += 1
                if user_guess < secret_number:
                    print("Your guess is too low.")
                elif user_guess > secret_number:
                    print("Your guess is too high.")
                else:
                    break

                if attempts < 6:
                    time.sleep(0.5)
                    print("Give it another try!")
            else:
                print("That number is out of the range! Please pick a number between 1 and 200.")
                time.sleep(0.25)
        except ValueError:
            print(f"{user_input} is not a valid number. Please enter a valid number.")

    if user_guess == secret_number:
        print(f"Congratulations, {player_name}! You guessed the number in {attempts} tries.")
    else:
        print(f"Sorry, the number I was thinking of was {secret_number}.")

play_again = "yes"
while play_again.lower() in ["yes", "y"]:
    welcome()
    guess_game()
    print("Would you like to play again?")
    play_again = input()
