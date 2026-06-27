# Hangman Game

A simple terminal-based Hangman game developed in Python.

This project is a basic implementation of the classic Hangman game where the player has to guess a randomly selected word by entering one letter at a time. The player has a limited number of attempts to complete the word before the game ends.

The purpose of this project was to strengthen my understanding of Python fundamentals and improve problem-solving skills through practical implementation.

## Features

* Random word selection for each game
* Tracks guessed letters
* Shows current word progress after every attempt
* Limits incorrect guesses
* Win and game-over conditions

## Built With

* Python 3
* Python `random` module

## How to Run

Clone the repository:

```bash id="4c0evl"
git clone https://github.com/your-username/hangman-game.git
```

Move into the project directory:

```bash id="qor5n7"
cd hangman-game
```

Run the program:

```bash id="9h7z3b"
python hangman.py
```

## How the Game Works

* The program selects a random word from a predefined list.
* The player enters one letter at a time.
* Correct guesses reveal the letter in the word.
* Incorrect guesses reduce the remaining attempts.
* The game continues until the word is guessed or all attempts are used.

## Learning Outcomes

While building this project, I worked on:

* Conditional statements
* Loops
* Lists and string operations
* User input handling
* Game logic implementation

## Future Enhancements

Possible improvements for future versions:

* Add input validation for invalid entries
* Expand the word list
* Introduce difficulty levels
* Add hints for players
* Build a graphical user interface

## License

This project is licensed under the MIT License.

## Author

Muhammad Mohsin Nehan

