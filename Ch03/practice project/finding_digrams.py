from collections import Counter
import load_dictionary

dictionary = load_dictionary.load("words.txt")

def find_digrams(word):
    """FInd digrams in a word."""
    letters = [char for char in word]
    digrams = []
    for i in range(0,len(word)-1):
        digrams.append(letters[i]+letters[i+1])
    return digrams

def main():
    voldemort = find_digrams("tmvoordle")
    master_digram_list = []
    for word in dictionary:
        digrams = find_digrams(word)
        for digram in digrams:
            if digram in voldemort:
                master_digram_list.append(digram)
    print(Counter(master_digram_list))
    
if __name__ == "__main__":
    main()
