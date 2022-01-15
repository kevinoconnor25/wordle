#!/usr/bin/python3

# Main file for running the game

import random
import sys
import word_lib

ENDC = '\033[0m'
RED = '\033[41m'
GREEN = '\033[42m'
YELLOW = '\033[43m'
GRAY = '\033[100m'

# Display the guess with proper colors based on position of letters
def display_output(answer, guess):
    answer_output = "\n"
    blocks = "\n"
    idx = 0
    for letter in guess:
        result = ""
        if letter == answer[idx]:
            result = GREEN + " %s " % letter + ENDC
            blocks += " " + GREEN + "  " + ENDC
        elif guess[idx] in answer:
            result = YELLOW + " %s " % letter + ENDC
            blocks += " " + YELLOW + "  " + ENDC
        else:
            result = GRAY + " %s " % letter + ENDC
            blocks += " " + GRAY + "  " + ENDC
        answer_output += " %s" % result
        idx += 1
    print(answer_output)

    return blocks + "\n"

# Get input and validate
def getInput(answer, words):
    guess = input("\nGuess: ")
    while guess not in words:
        if guess == "?":
            printHelp(answer, words)
        guess = input("Not a valid word. Guess again: ")
    return guess

# Print a list of all possible answers
def printHelp(answer, words):
    # Could be tough. Need a method that takes the answer and list of all words and returns all possible answers based on clues. That means I probably need to pass in the difficuly too.
    print("Possible answers: ")
    print(answer)

def main():
    # Game configuration should be read from a wordle.conf (JSON?) file

    # Number of letters in the answer
    num_letters = 5
    if len(sys.argv) > 1:
        num_letters = int(sys.argv[1])

    # Maximum number of times the user can guess the answer. This should be (num_letters-2)*2 or 4, whichever is greater
    max_guesses = (num_letters- 2) * 2

    # Level of difficulty:
    # "easy" has subset of dictionary containing more common words
    # "normal" has standard dictionary and no guessing restrictions
    # "hard" has standard dictionary but user is forced to use hints
    difficulty = "normal"

    # Whether there is a timer. True is "on", false is "off"
    timer = "off"

    words = word_lib.get_words(num_letters)
    answer = words[random.randrange(len(words))]
    num_guesses = 0
    guess = ""
    blocks = ""
    correct = False

    print("Starting game with the following parameters:")
    print("LETTERS:    %s" % num_letters)
    print("GUESSES:    %s" % max_guesses)
    print("DIFFICULTY: %s" % difficulty)
    print("TIMER:      %s" % timer)

    # Main loop
    while(num_guesses < max_guesses and correct == False):
        guess = getInput(answer, words)
        blocks += display_output(answer, guess)
        if guess == answer:
            correct = True
        num_guesses += 1

    if correct == True:
        print("\nWordle %s/%s" % (num_guesses, max_guesses))
    else:
        print("Close! Answer was %s" % answer)

    print(blocks)

main()
