import random

# List of predefined words
words_list = ["laptop", "table", "chair", "mouse", "computer"]

# Randomly selection of one word
secret_word = random.choice(words_list)

guessed_letters = []
wrong_attempts = 0
max_attempts = 6

print("Welcome to the Hangman Game!")

# while loop for the game
while wrong_attempts < max_attempts:

    display_word = ""

    # Shows guessed letters and hide remaining letters
    for letter in secret_word:
        if letter in guessed_letters:
            display_word = display_word + letter
        else:
            display_word = display_word + "_"

    print("Word:", display_word)

    # Checks if user guessed the full word 
    if display_word == secret_word:
        print("You won! The word was:", secret_word)
        break

    # Take user input
    guess = input("Enter a letter: ")

    # Check if input is already guessed
    if guess in guessed_letters:
        print("You already guessed this letter.")

    # Check if guess is correct
    elif guess in secret_word:
        guessed_letters.append(guess)
        print("Correct Guess!")

    # Wrong guess
    else:
        guessed_letters.append(guess)
        wrong_attempts = wrong_attempts + 1
        print("Wrong Guess!")
        print("Remaining attempts:", max_attempts - wrong_attempts)

# If user loses
if wrong_attempts == max_attempts:
    print("Game Over!")
    print("The correct word was:", secret_word)