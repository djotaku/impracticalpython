"""Identify whether a cipher is letter-transposition or letter-substitution."""
from collections import Counter
import pprint

def import_cipher(filename):
    with open(filename, 'r') as file:
        return "".join(file.readlines())


def analyze_cipher(cipher):
    counter = Counter()
    for letter in cipher:
        counter[letter] += 1
    print(counter.most_common(10))
    return counter.most_common(10)
        


def main():
    cipher_a = import_cipher('cipher_a.txt')
    cipher_a_analysis = analyze_cipher(cipher_a)
    if cipher_a_analysis[0][0] == 'E' and cipher_a_analysis[1][0] == 'T' and cipher_a_analysis[2][0] == 'A':
        print("Almost certainly a transposition.")
    elif cipher_a_analysis[0][0] == 'E' and cipher_a_analysis[1][0] == 'T':
        print("Even likelier to be a transposition.")
    elif cipher_a_analysis[0][0] == 'E':
        print("Likely to be transposition.")
    else:
        print("Probably substitution")
    
    cipher_b = import_cipher('cipher_b.txt')
    cipher_b_analysis = analyze_cipher(cipher_b)
    if cipher_b_analysis[0][0] == 'E' and cipher_b_analysis[1][0] == 'T' and cipher_b_analysis[2][0] == 'A':
        print("Almost certainly a transposition.")
    elif cipher_b_analysis[0][0] == 'E' and cipher_b_analysis[1][0] == 'T':
        print("Even likelier to be a transposition.")
    elif cipher_b_analysis[0][0] == 'E':
        print("Likely to be transposition.")
    else:
        print("Probably substitution")
    
        

if __name__ == "__main__":
    main()
