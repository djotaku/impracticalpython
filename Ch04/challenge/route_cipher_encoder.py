"""Encrypt a message with a route cipher."""

phrase_to_encrypt = "We will run the batteries at Vicksburg the night of April 16 and proceed to Grand Gulf where we will reduce the forts. Be prepared to cross the river on April 25 or 29. Admiral Porter."

code_word_dictionary = dict([("BATTERIES", "HOUNDS"), ("VICKSBURG", "ODOR"), ("APRIL", "CLAYTON"), ("16", "SWEET"), ("GRAND","TREE"), ("GULF", "OWL"), ("FORTS", "BAILEY"), ("RIVER", "HICKORY"), ("25", "MULTIPLY"), ("29", "ADD"), ("ADMIRAL", "HERMES"), ("PORTER", "LANGFORD") ])

key = [-1, 3, -2, 6, 5, -4]

ROWS = 6

COLS = 7

phrase_as_list = phrase_to_encrypt.split()

# remove periods
phrase_as_list = [word.rstrip('.') for word in phrase_as_list]

for word in phrase_as_list:
    if word.upper() in code_word_dictionary.keys():
        phrase_as_list[phrase_as_list.index(word)] = code_word_dictionary[word.upper()]

matrix = []

START = 0
STOP = COLS

for number in range(0, ROWS):
    matrix.append(phrase_as_list[START:STOP])
    START += COLS
    STOP += COLS
    
for number in range(1, COLS + 1):
    matrix[5].append('FILLER')
    

encoded_message = ''

for number in key:
    current_col = []
    for row in matrix:
        current_col.append(row[abs(number)-1])
    if number > 0:
        encoded_message += ' '.join(current_col)
    elif number < 0:
        encoded_message += ' '.join(reversed(current_col))

print(encoded_message)
