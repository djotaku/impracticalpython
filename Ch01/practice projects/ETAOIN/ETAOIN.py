"""Takes in a sentence and creates a Poor Man's Bar Chart."""
from collections import defaultdict
import pprint

def main():
    """Run the code to create the bar chart."""
    sentence = input("Give me a sentence to analyze: ")
    pp = pprint.PrettyPrinter(indent=4)
    d = defaultdict(list)
    for letter in sentence.lower():
        if letter == " ":
            pass
        else:
            d[letter].append(letter)
    pp.pprint(d)

if __name__ == "__main__":
    main()
