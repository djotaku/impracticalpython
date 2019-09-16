"""Takes in a word from the user and returns it in Pig Latin."""

def main():
    """Asks for sentence and pig-latinizes it. Will break with punctuation."""
    sentence = input("Give me a sentence! \n\n")
    words = sentence.split()
    print("Pig Latin:")
    for word in words:
        piglatin(word)

def piglatin(normal):
    """Convert the word to Pig Latin."""    
    vowels = ['a', 'e', 'i', 'o', 'u']
    if normal[0].lower() in vowels:
        print(f"{normal}way ")
    else:
        print(f"{normal[1:]}{normal[0]}ay ")

if __name__ == "__main__":
    main()
