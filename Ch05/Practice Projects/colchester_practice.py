"""Find a Trevanion-type null cipher encoded with a specific number of letters after each punctuation mark."""

import sys

def load_text(file):
    """Load a text file as a string."""
    with open(file) as f:
        return f.read().strip()  # strip removes leading and trailing whitespace


def solve_null_cipher(message, nth):
    """ Solve a null cipher based on number of letters the nth word.
    
    message = null cipher text as a string stripped of whitespace
    nth = the nth letter of the nth word to check
    """
    for i in range(1, nth + 1):
        print(f"Using increment letter {nth} of word {nth}")
        print()
        count = i - 1
        location = i - 1
        for index, word in enumerate(message):
            if index == count:
                if location < len(word):
                    print(f"letter = {word[location]}")
                    count += i
                else:
                    print("interval doesn't work", file=sys.stderr)


def main():
    """Load text, solve null cipher."""
    # load & process message:
    filename = "colchester.txt"
    try:
        loaded_message = load_text(filename)
    except IOError as e:
        print("{}. Terminating program.".format(e), file=sys.stderr)
        sys.exit(1)
    print("\nORIGINAL MESSAGE = ")
    print(f"{loaded_message} \n")
    
    # remove whitespace
    message = loaded_message.split()
    
    # get range of possible cipher keys from user:
    while True:
        lookahead = input("\nGive me n for nth letter of every nth word: ")
        if lookahead.isdigit():
            lookahead = int(lookahead)
            break
        else:
            print("Please input a number.", file=sys.stderr)
        print()
            
    # run function to decode cipher
    solve_null_cipher(message, lookahead)

if __name__ == "__main__":
    main()
