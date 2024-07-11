# NumberGuess
This is a Python-based number guessing game where the player tries to guess a randomly chosen number between 1 and 200. The player has up to six attempts to guess the correct number. After each guess, the game provides feedback indicating whether the guess is too low, too high, or correct. The game includes an option to play again after each round.

Modules
random: Used to generate a random number.
time: Used to add delays to improve the user experience.
Functions
1. welcome()
Description: Greets the player and explains the game.

Parameters: None

Returns: None

Behavior:

Prompts the player to enter their name.
Welcomes the player by name and explains the game rules.
Adds a short delay for a better user experience.
2. guess_game()
Description: Manages the core guessing game logic.

Parameters: None

Returns: None

Behavior:

Sets the number of attempts to 0.
Runs a loop to allow the player up to six guesses.
Prompts the player to enter a guess.
Validates the guess to ensure it is an integer within the range of 1 to 200.
Provides feedback if the guess is too low, too high, or correct.
Informs the player if the number is out of range or not a valid integer.
Tracks the number of attempts.
Congratulates the player if they guess correctly within six attempts.
Reveals the correct number if the player fails to guess it within six attempts.
Main Loop
The main loop allows the player to play the game multiple times. After each round, the player is asked if they would like to play again. If the player responds with "yes" or "y", the game restarts.
