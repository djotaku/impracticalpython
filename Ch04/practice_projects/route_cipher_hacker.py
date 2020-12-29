"""Attempt to brute force route transposition cipher."""

from permutations import key_permutations

"""Decrypt a path through a Union Route Cipher.

Desgined for whole-word transposition ciphers with variable rows & columns.
Assumes encryption began at either top or bottom of ao column.
Key indicates the order to read columns and the direction to traverse.
Negative column numbers mean start at the bottom and read up.
Positive column numbers mean start at the top and read down.

Example below is for 4x4 matrix with key -1 2 -3 4.
Note '0' is not allowed.
Arrows show encryption route; for negative key values, read UP.

  1   2   3   4
  _   _   _   _
| ^ | | | ^ | | | MESSAGE IS WRITTEN
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | ACROSS EACH ROW
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | IN THIS MANNER
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | LAST ROW IS FILLED WITH DUMMY WORDS
|_|_|_v_|_|_|_v_|
START        END

Required inputs - a text message, # of columsn, # of rows, key string

Prinst translated plaintext.
"""
import sys
#==========================================================================
# USER INPUT:

# the string to be decrypted (type or paste between triple-quotes):
ciphertext = """THIS OFF DETAINED ASCERTAIN WAYLAND CORRESPONDENTS OF AT WHY AND IF FILLS IT YOU GET THEY NEPTUNE THE TRIBUNE PLEASE ARE THEM CAN UP
"""

# number of columns in the transposition matrix:
COLS = 4

# number of rows in the transposition matrix
ROWS = 6

# key with spaces between numbers; negative to read UP column (ex = -1 2 -3 4):
keys = key_permutations(4)

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
#==========================================================================

def main():
    """Run program and print decrypted plaintext."""
    print(f"\n Ciphertext = {ciphertext}")
    print(f"Trying {COLS} columns.")
    print(f"Trying {ROWS} rows.")
    
    
    for key in keys:
        print(f"Trying {key=}")
    
        # split elements into words, not letters
        cipherlist = list(ciphertext.split())
        validate_col_row(cipherlist)
        key_int = key_to_int(key)
        translation_matrix = build_matrix(key_int, cipherlist)
        plaintext = decrypt(translation_matrix)
    
        print(f"Plaintext = {plaintext}")
    
def validate_col_row(cipherlist):
    """Check that input columns & rows are valid vs. message length."""
    factors = []
    len_cipher = len(cipherlist)
    for i in range(2, len_cipher):  # range excludes 1-column ciphers
        if len_cipher % i == 0:
            factors.append(i)
    print(f"\nLength of cipher = {len_cipher}")
    print(f"Acceptable column/row values included: {factors}")
    print()
    if ROWS * COLS != len_cipher:
        print("\nError - Input columns & rows not facotrs of length. of cipher. Terminating Program.", file=sys.stderr)
        sys.exit(1)

def key_to_int(key):
    """Turn key into list of integers and check validity."""
    key_int = key
    key_int_low = min(key_int)
    key_int_hi = max(key_int)
    if len(key_int) != COLS or key_int_low < -COLS or key_int_hi > COLS or 0 in key_int:
        print("\nError - Problem with key. Terminating.", file=sys.stderr)
        sys.exit(1)
    else:
        return key_int

def build_matrix(key_int, cipherlist):
    """Turn every n items in a list into a new item in a list of lists."""
    translation_matrix = [None] * COLS
    start = 0
    stop = ROWS
    for k in key_int:
        if k < 0: # read column bottom-to-top
            col_items = cipherlist[start:stop]
        elif k > 0: # read column top-to-bottom
            col_items = list((reversed(cipherlist[start:stop])))
        translation_matrix[abs(k) - 1] = col_items
        start += ROWS
        stop += ROWS
    return translation_matrix

def decrypt(translation_matrix):
    """Loop through nested lists popping off last item to a sting."""
    plaintext = ''
    for i in range(ROWS):
        for matrix_col in translation_matrix:
            word = str(matrix_col.pop())
            plaintext += word + ' '
    return plaintext


if __name__ == "__main__":
    main()
