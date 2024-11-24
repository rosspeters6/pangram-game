#
# This script picks a pangram randomly from a list of words.
# When it runs, it prints the letters and the line number
# of the word in the input file.
#
# This script doesn't keep its own list of words data structure.
# Instead, it keeps picking words at random from the file until
# it finds a word with the desired number of letters.
#
import argparse
import linecache
import os
import random
import time

# Parse inputs.
parser = argparse.ArgumentParser(
                    prog='Pangram Game',
                    description='Finds random pangram and scrambles word.',
                    epilog='File must contain at least one pangram word.')
parser.add_argument('-f',
                    '--file',
                    help='Path to list of words',
                    type=str,
                    default='/usr/share/dict/words')
parser.add_argument('-u',
                    '--unique-letters',
                    help='Number of unique letters in pangram word',
                    type=int,
                    default=7)
parser.add_argument('-l',
                    '--length-min',
                    help='Minimum length of pangram word',
                    type=int,
                    default=12)
parser.add_argument('-d',
                    '--debug',
                    help='Set to print debug messages',
                    action='store_true',
                    default=False)
args = parser.parse_args()
LIST_OF_WORDS_FILENAME = args.file
PANGRAM_UNIQUE_LETTER_COUNT = args.unique_letters
PANGRAM_MIN_WORD_LENGTH = args.length_min
DEBUG_PRINTS_ENABLED = args.debug

# This script assumes the file contais at least one word that has
# the special number of unique letters.

# Get number of words in file.
assert os.path.exists(LIST_OF_WORDS_FILENAME)
with open(LIST_OF_WORDS_FILENAME) as list_of_words_file:
    for i, _ in enumerate(list_of_words_file):
        pass
number_of_words_in_file = i + 1

# Find a random word in the list with the desired number of unique letters.
iterations = 0
search_start_time = time.process_time()
while True:
    # Pick a random word.
    word_line_number = random.randint(1, number_of_words_in_file)
    word = linecache.getline(LIST_OF_WORDS_FILENAME, word_line_number).rstrip()
    unique_letters_in_word = set(word)

    # Make sure it's a pangram.
    has_unique_letter_count = (
        len(unique_letters_in_word) == PANGRAM_UNIQUE_LETTER_COUNT)
    has_minimum_length = (len(word) >= PANGRAM_MIN_WORD_LENGTH)
    is_pangram = has_minimum_length and has_unique_letter_count
    iterations += 1
    if is_pangram:
        break
    # If a pangram wasn't found, pick another random word.
search_end_time = time.process_time()
search_time = search_end_time - search_start_time

if DEBUG_PRINTS_ENABLED:
    print(f'Pangram word is: {word}')
    print(f'Found in {iterations} loops, {search_time:.6f} seconds.')

# Scramble unique letters in word and print it.
shuffled_unique_letters_as_list = list(unique_letters_in_word)
random.shuffle(shuffled_unique_letters_as_list)
shuffled_unique_letters = ''.join(shuffled_unique_letters_as_list)
print(shuffled_unique_letters.upper())
