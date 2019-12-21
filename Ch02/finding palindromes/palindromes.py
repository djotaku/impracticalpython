"""Find palindromes (letter palingrames) in a dictionary file."""

import load_dictionary
word_list = load_dictionary.load('words.txt')
pali_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

print(f"\nNumber of Palindromes found = {len(pali_list)}\n")
print(*pali_list, sep='\n') 
# splat operator takes a list as inport and expands it into positional arguments.
# sep tells how to separate the palindromes. In this case, one per line.
# this is more efficient than a for loop.
