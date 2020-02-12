import load_dictionary

word_list = load_dictionary.load('words.txt')

anagram_list = []

# input a SINGLE word or SINGLE name below to find its anagram(s):
name = "Foster"
print(f"Input name = {name}")
name = name.lower()
print(f"Using name = {name}")

# sort name & find anagrams
name_sorted = sorted(name)
for word in word_list:
    word = word.lower()
    if word != name:
        if sorted(word) == name_sorted:
            anagram_list.append(word)
            
# print out list of anagrams
print()
if len(anagram_list) == 0:
    print("You need a larger dictionary or a new name!")
else:
    print("Anagrams =", *anagram_list, sep='\n') # a reminder that the splat allows for printing each member of a list
