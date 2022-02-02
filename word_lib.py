#!/usr/bin/python3

# word_lib
#
# Library containing methods for retrieving list of words for a given round

import json
import os
import re

with open("wordle.conf") as config:
    params = json.load(config)

WORDS_FILE = params["dictionaries"]["base-dict"]

# Gets passed the number of letters in the answer and returns the list of valid words with the same number of letters
def get_words(num_letters):
    filepath = "dicts/%s-letter-words.txt" % num_letters
    if not(os.path.exists(filepath)):
        create_words_file(num_letters)

    words_file = open(filepath, 'r')
    words = []
    for line in words_file:
        words.append(line.strip())
    words_file.close()

    return words


# Create a text file containing all valid words with a certain number of letters, all separated by newlines
def create_words_file(num_letters):
    print("Creating new txt file containing valid words with %s letters..." % num_letters)
    new_file_content = ""
    new_filepath = "dicts/%s-letter-words.txt" % num_letters
    words_file = open(WORDS_FILE, 'r')

    # Regular expression to match words with num_letters letters
    regex = "^[a-z]{%s}$" % num_letters

    for word in words_file:
        if re.match(regex, word):
            new_file_content += word
    words_file.close()

    new_file = open(new_filepath, "w")
    new_file.write(new_file_content)
    new_file.close()
