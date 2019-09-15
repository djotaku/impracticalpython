"""Takes in a word from the user and returns it in Pig Latin."""
 
def main():
    word = input("Give me a word! \n\n")
    vowels = ['a','e','i','o','u']
    if word[0].lower() in vowels:
        print(f"\n\nPig latin: {word}way")
    else:
        print(f"{word[1:]}{word[0]}ay")
         
if __name__ == "__main__":
    main()
