import sys
from string import punctuation
import json
from nltk.corpus import cmudict

# load dictionary of words in haiku corpus, but not in cmudict
with open('missing_words.json') as f:
    missing_words = json.load(f)
    
cmudict = cmudict.dict()

def count_syllables(words):
    """Use corpora to count syllables in English word or phrase."""
    # prep words for cmudict corpus
    woreds = words.replace('-', ' ')
    words = words.lower().split()
    num_sylls = 0
    for word in words:
        word = word.strip(punctuation)
        if word.endswith("'s") or word.endswith("’s"):
            word = word[:-2]
        if word in missing_words:
            num_sylls += missing_words[word]
        else:
            for phonemes in cmudict[word][0]:  # first one in case there's more than one pronounciation
                for phoneme in phonemes:
                    if phoneme[-1].isdigit():  # if you find a digit at the end of the string, you know it's a vowel
                        num_sylls += 1
    return num_sylls

def main():
    while True:
        print("Syllable Counter")
        word = input("Enter word or phrase; else press Enter to Exit: ")
        if word == "":
            sys.exit()
        try:
            num_syllables = count_syllables(word)
            print(f"Number of syllables in {word} is {num_syllables}")
            print()
        except KeyError:
            print("Word not found. Try again.\n", file=sys.stderr)


if __name__ == "__main__":
    main()
