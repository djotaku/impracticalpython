"""Hide a message from Mary, Queen of Scots, using a null cipher in a list of surnames."""

from random import randint
import string
import load_dictionary


# Alternate between second and third letter of the name
# throw Stuart and Jacob in the list, but don't use them to hide letters
# throw in a short message not part of the cypher

intro_message = "A list of those we can count on in times of trouble."

null_names = ['Stuart', 'Jacob']

input_message = "Give your word and we rise"

message = ''
for char in input_message:
    if char in string.ascii_letters:
        message += char
print(message, '\n')
message = "".join(message.split())

# open dictionary file
word_list = load_dictionary.load('supporters.txt')

# build vocabulary word list with hidden message
supporter_list = []
for count, letter in enumerate(message):
    for word in word_list:
        if count % 2 == 0:
            if word[2].lower() == letter.lower() and word not in supporter_list:
                supporter_list.append(word)
                break
        else:
            if word[1].lower() == letter.lower() and word not in supporter_list:
                supporter_list.append(word)
                break

null_position_1 = randint(0, 4)
null_position_2 = randint(5,10)

supporter_list.insert(null_position_1, null_names[0])
supporter_list.insert(null_position_2, null_names[1])

if len(supporter_list) < len(message):
    print("Word list is too small. Try larger dictionary or shorter message!")
else:
    print(f"{intro_message}\n", *supporter_list, sep="\n")



# add the null_names. I was thinking that after the list was made, use randint to pick a random spot (early in the list) to insert the names - use list.insert
