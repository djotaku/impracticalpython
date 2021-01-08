# What I learned - Chapter 5 - Encoding English Civil War Ciphers

This chapter is about steganography. Rather than the image version I arlready knew about, this is the version where you look at, say, the first letter of each word.

## About Cryptography

- it's a lot easier to read a null cipher than it is to create one. The one we create in project 11 would need another randomizer because I think it's kind of suspicious that all the vocab words are from the "a" section in alphabetical order.


## About Python

- use the string module to get access to the ability to idenfify letters and punctuation without the need for regular expressions!  (see null_cipher_finder.py and list_cipher.py)
- you and use strip() as you're reading in a file instead of as a separate step (see null_cipher_finder.py)
- randint() function from random module - works better than some inelegant workarounds I've used in the past
