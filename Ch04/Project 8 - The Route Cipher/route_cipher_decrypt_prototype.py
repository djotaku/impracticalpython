#########################################
# this first part is from a control message so that you can make sure your decryption code works - ERM

ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"

# split elements into words, not letters

cipherlist = list(ciphertext.split()) # doesn't split return a list already? Isn't this redundant? Maybe it used to work differently? -ERM

# initialize variables
COLS = 4
ROWS = 5
key = '-1 2 -3 4' # neg nubmer means read UP column vs DOWN
translation_matrix = [None] * COLS  # initializing with NONEs so that you can use the indexes to place items in various places (had do to this during AoC 2020) - ERM
plaintext = ''
start = 0
stop = ROWS
############################################


# turn key_int into list of integers:
key_int = [int(i) for i in key.split()]  # see, here he doesn't use list... - ERM

# turn columns into  items in list of lists:
for k in key_int:
    if k < 0: # reading bottom-to-top of column
        col_items = cipherlist[start:stop]
    elif k > 0: # reading top-to-bottom of column
        col_items = list((reversed(cipherlist[start:stop])))
    translation_matrix[abs(k) - 1] = col_items
    start += ROWS
    stop += ROWS
    
    print(f'\n{ciphertext=}')
    print('\ntranslation matrix =,, *translation_matrix, sep="\n"')
    print(f'\nnkey length = {len(key_int)}')
    
    # loop through nested lists popping off last item to new list:
    for i in range(ROWS):  # just learned in the Python Morsels I did today that this assumes a start of 0 and a step of 1
        for col_items in translation_matrix:
            word = str(col_items.pop())
            plaintext += word + ' '
    
    print(f'{plaintext=}')
