#!/usr/bin/python3

# Main file for running the game

import json
import random
import sys
import word_lib

ENDC = "\033[0m"
RED = "\033[41m"
GREEN = "\033[42m"
YELLOW = "\033[43m"
GRAY = "\033[100m"

# Get a dictionary of unique letters and their count
def getUniqueDict(answer):
    letters = {}
    for letter in answer:
        if letter not in letters.keys():
            letters[letter] = answer.count(letter)
    return letters

# Display the guess with proper colors based on position of letters
def display_output(answer, guess):
    answer_output = "\n"
    blocks = "\n"
    _idx = 0
    idx = 0
    letterCounts = getUniqueDict(answer)

    # Deduct greens from count
    for _letter in guess:
        if _letter== answer[_idx]:
            letterCounts[_letter] -= 1
        _idx += 1

    # Display the guess and deduct yellows from count
    for letter in guess:
        result = ""
        if letter == answer[idx]:
            result = GREEN + " %s " % letter + ENDC
            blocks += " " + GREEN + "  " + ENDC
        elif guess[idx] in answer and letterCounts[letter] > 0:
            letterCounts[letter] -= 1
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
    with open("wordle.conf") as config:
        params = json.load(config)["level-parameters"]

    # Number of letters in the answer
    num_letters = params["letters"]
    if len(sys.argv) > 1:
        num_letters = int(sys.argv[1])

    # Maximum number of times the user can guess the answer. 6 seems to be a perfect number no matter the number of letters
    max_guesses = params["guesses"]

    # Level of difficulty:
    # "easy" has subset of dictionary containing more common words
    # "normal" has standard dictionary and no guessing restrictions
    # "hard" has standard dictionary but user is forced to use hints
    difficulty = params["difficulty"]

    # Whether there is a timer. True is "on", false is "off"
    timer = params["timer"]

    print("Starting game with the following parameters:")
    print("LETTERS:    %s" % num_letters)
    print("GUESSES:    %s" % max_guesses)
    print("DIFFICULTY: %s" % difficulty)
    print("TIMER:      %s" % timer)

    words = word_lib.get_words(num_letters)
    answer = words[random.randrange(len(words))]
    num_guesses = 0
    guess = ""
    blocks = ""
    correct = False

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
        print("\nWordle X/%s, Answer was %s" % (max_guesses, answer))

    print(blocks)

if __name__ == '__main__':
    main()
