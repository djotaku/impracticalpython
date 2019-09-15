"""Takes in a word from the user and returns it in Pig Latin."""
 
def main():
    word = input("Give me a word! ")
    if word[0].lower() == "a" or word[0].lower() == "e" or word[0].lower() == "i" or word[0].lower() == "o" or word[0].lower() == "u":
        print("vowel")
         
if __name__ == "__main__":
    main()
