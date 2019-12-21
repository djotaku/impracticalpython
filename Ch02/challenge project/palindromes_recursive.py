"""Find palindromes (letter palingrames) in a dictionary file."""

import load_dictionary
word_list = load_dictionary.load('words.txt')
pali_list = []

def is_palindrome(word):
    if len(word) ==0:
        return True
    elif len(word) == 1:
        return True
    elif word[0] == word[-1]:
        return is_palindrome(word[1:-1]) # having return here is key to recursion working
    else:
        return False

for word in word_list:
    if is_palindrome(word):
        pali_list.append(word)

print(f"\nNumber of Palindromes found = {len(pali_list)}\n")
print(*pali_list, sep='\n') 
# splat operator takes a list as inport and expands it into positional arguments.
# sep tells how to separate the palindromes. In this case, one per line.
# this is more efficient than a for loop.
