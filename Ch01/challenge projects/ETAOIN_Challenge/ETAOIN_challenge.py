"""Takes in a sentence and creates a Poor Man's Bar Chart. However, this version displays every letter of the alphabet in order to compare letters better."""
from collections import defaultdict
import pprint

def main():
    """Run the code to create the bar chart."""
    Alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentence = input("Give me a sentence to analyze: ")
    pp = pprint.PrettyPrinter(indent=4)
    d = defaultdict(list)
    for letter in sentence.lower():
        if letter == " ":
            pass
        else:
            d[letter].append(letter)
    not_sentence = set(Alphabet) - set(sentence.lower())
    for letter in not_sentence:
        d[letter].append("")
    pp.pprint(d)

if __name__ == "__main__":
    main()
