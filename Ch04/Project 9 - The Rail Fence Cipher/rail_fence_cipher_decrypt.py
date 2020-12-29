r"""Decrypt a Civil War 'rail fence' type cipher.

This is for a "2-rail" fence cipher for short messages.

Example text to encrypt: ' Buy more Main potatoes'

Rail fence style B Y O E A N P T T E
                  U M R M I E O A O S

Reaad zizag      \/\/\/\/\/\/\/\/\/\/

Encrypted: BYOEA NPTTE UMRMI EOSOS

"""
import math
import itertools
#---------------------------------------------------
# USER INPUT: 

# the string to be decrypted (paste between quotes):
ciphertext = """LTSRS OETEI EADET NETEH DOTER EEUCO SVRHR VRNRS UDRHS AEFHT ES
"""
# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
#----------------------------------------------------------------------------------

def main():
    """Run program to decrypt 2-rail rail fence cipher."""
    message = prep_ciphertext(ciphertext)
    row1, row2 = split_rails(message)
    decrypt(row1, row2)

def prep_ciphertext(ciphertext):
    """Remove whitespace."""
    message = "".join(ciphertext.split())
    print(f"\n{ciphertext=}")
    return message

def split_rails(message):
    """Split message in two, always rounding UP for 1st row."""
    row_1_len = math.ceil(len(message)/2)
    row1 = (message[:row_1_len])
    row2 = (message[row_1_len:])
    return row1, row2

def decrypt(row1, row2):
    """Build list with every other letter in 2 strings and print."""
    plaintext = []
    for r1, r2 in itertools.zip_longest(row1, row2):
        plaintext.append(r1.lower())
        plaintext.append(r2.lower())
    if None in plaintext:  # the zip_longest would insert a None where the shorter and longer lists don't line up. So we want to remove it. 
        plaintext.pop()
    print(f"rail 1 = {row1}")
    print(f"rail 2 = {row2}")
    print("\nplaintext = {}".format(''.join(plaintext)))
    

if __name__ == "__main__":
    main()
