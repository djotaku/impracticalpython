import load_dictionary

word_list = load_dictionary.load('words.txt')

one_letter_words = ['a','i']

new_word_list = []

for word in word_list:
   if word in one_letter_words:
       new_word_list.append(word)
   elif len(word) > 1:
        new_word_list.append(word)
        

print(*new_word_list,"\n")
