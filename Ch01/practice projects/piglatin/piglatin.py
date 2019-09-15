"""Takes in a word from the user and returns it in Pig Latin."""
 
def main():
    word = input("Give me a word! ")
    vowels = ['a','e','i','o','u']
    if word[0].lower() in vowels:
        print("vowel")
         
if __name__ == "__main__":
    main()
