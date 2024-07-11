This Python-based number guessing game challenges players to guess a randomly chosen number between 1 and 200. The player has up to six attempts to guess the number correctly. Feedback is provided for each guess, indicating whether it is too low, too high, or correct. The game can be replayed multiple times based on the player's choice.
Modules and Libraries
•	random: Used to generate a random number between 1 and 200.
•	time: Used to introduce delays to enhance the user experience.
Variables
•	secret_number: A random number between 1 and 200, generated at the start of the game using random.randint(1, 200).
Functions
1. welcome()
Description: Greets the player and provides instructions for the game.
Parameters: None
Returns: None
Behavior:
•	Prompts the player to enter their name.
•	Welcomes the player and explains that they need to guess a number between 1 and 200.
•	Introduces a brief delay to improve the user experience.
2. guess_game()
Description: Manages the core logic of the guessing game.
Parameters: None
Returns: None
Behavior:
•	Initializes the attempts counter to 0.
•	Runs a loop that allows the player up to six attempts to guess the number.
•	Prompts the player to enter a guess and validates the input:
o	If the input is not a valid integer, it prompts the player to enter a valid number.
o	If the guess is outside the range of 1 to 200, it prompts the player to pick a number within the range.
•	Provides feedback:
o	Indicates whether the guess is too low or too high.
o	If the guess is correct, breaks the loop.
•	After the loop, checks if the player guessed correctly:
o	Congratulates the player if they guessed the number within six attempts.
o	Reveals the secret number if they did not guess correctly.
Main Loop
The main loop of the game allows the player to play multiple rounds. It performs the following actions:
1.	Sets play_again to "yes".
2.	While play_again is "yes" or "y":
o	Calls the welcome() function to greet the player and explain the rules.
o	Calls the guess_game() function to run the guessing game.
o	Asks the player if they want to play again.
o	Reads the player's response and updates play_again.
How to Play
1.	Run the program: Execute the Python script to start the game.
2.	Enter your name: When prompted, input your name.
3.	Guess the number: Enter your guess when prompted. The game will tell you if your guess is too low, too high, or correct.
4.	Continue guessing: Keep guessing until you either guess the number correctly or exhaust your six attempts.
5.	Play again: After the game ends, you will be asked if you want to play again. Enter "yes" or "y" to play again, or any other key to exit.
Enjoy playing the Number Guessing Game!


