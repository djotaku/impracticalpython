import sys
from string import punctuation
import pprint
import json
from nltk.corpus import cmudict

cmudict = cmudict.dict()  # Carnegie Mellon University Pronouncing Dictionary - words are keys and phonemes are values

def main():
    haiku = load_haiku('train.txt')
    exceptions = cmudict_missing(haiku)
    build_dict = input("\nManually build an exceptions dictionary (y/n)? \n")
    if build_dict.lower() == 'n':
        sys.exit()
    else:
        missing_words_dict = make_exceptions_dict(exceptions)
        save_exceptions(missing_words_dict)


def load_haiku(filename):
    """Open and return training corpus of haiku as a set."""
    with open(filename) as in_file:
        haiku = set(in_file.read().replace('-',' ').split())  # replace hyphen with space
        return haiku
    

def cmudict_missing(word_set):
    """Find and return words in a word set missing from cmudict."""
    exceptions = set()
    for word in word_set:
        word = word.lower().strip(punctuation)
        if word.endswith("'s") or word.endswith("`s"):
            word = word[:-2]
        if word not in cmudict:
            exceptions.add(word)
    print("\nexceptions:")
    print(*exceptions, sep='\n')
    print(f"\nNumber of unique words in haiku corpus = {len(word_set)}")
    print(f"Number of words in corpus not in cmudict = {len(exceptions)}")
    membership = (1 - (len(exceptions) / len(word_set))) * 100
    print(f"cmudict membership = {membership:.1f}%")
    return exceptions


def make_exceptions_dict(exceptions_set):
    """Return dictionary of words & syllable counts form a set of words."""
    missing_words = {}
    print("Input # syllables in word. Mistakes can be corrected at end. \n")
    for word in exceptions_set:
        while True:
            num_sylls = input(f"Enter number syllables in {word}")
            if num_sylls.isdigit():
                break
            else:
                print("        Not a valid answer!", file=sys.stderr)
        missing_words[word] = int(num_sylls)
        print()
        pprint.pprint(missing_words, width=1)
        
        print("\nMake Changes to Dictionary Before Saving?")
        print("""
            0 - Exit and Save
            1 - Add a Word of Change a Syllable Count
            2 - Remove a Word
            """)
        
        while True:
            choice = input("\nEnter Choice: ")
            if choice == '0':
                break
            elif choice == '1':
                word = input("\nWord to add or change: ")
                missing_words[word] = int(input(f"Enter number of syllsables in {word}:"))
            elif choice == '2':
                word = input("\nEnter word to delete: ")
                missing_words.pop(word, None)  # None means there won't be a KeyError if the user enters a word not in the dict
        
        print("\nNew woreds of syllable changes:")
        pprint.pprint(missing_words, width=1)
        
        return missing_words

def save_exceptions(missing_words):
    """Save exceptions dictionary as json file."""
    json_string = json.dumps(missing_words)
    with open('missing_words.json', 'w') as f:
        f.write(json_string)
    print("\nFile saved as missing_words.json")


if __name__ == "__main__":
    main()
