"""Take a dictionary file and have a user choose how many words to test against syllable counter. Display words and syllable count."""

import random

import count_syllables

with open('dictionary_file.txt') as file:
    dictionary_words = [word.strip('\n') for word in file.readlines()]

how_many_words = int(input("How many words should be chosen from the dictionary? "))  # not going to do defensive programming here

while how_many_words > 0:
    word = random.choice(dictionary_words)
    try:
        syllable_count = count_syllables.count_syllables(word)
        print(word, syllable_count, end='\n')
    except KeyError:
        print(f"Sorry, {word} is not in the syllable counting database.")
    how_many_words -= 1
