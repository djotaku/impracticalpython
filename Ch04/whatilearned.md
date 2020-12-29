# What I Learned

## Crypto

- A code replaces whole words with whole words. A cipher replaces or scrambles letters
- Transposition cipher scrambles arrangement of letters or words rather than replacing the letters.

## Python

- A good exmaple of how to document code where users will be opening up the code to run it. (Possible with languages like Python, Ruby, etc) - see [route_cipher_decrypt.py](https://github.com/djotaku/impracticalpython/blob/master/Ch04/Project%208%20-%20The%20Route%20Cipher/route_cipher_decrypt.py)
- using an 'r' before a multiline docstring allows it to ignore slashes (which it would othewrise interpret as special characters. - see [rail_fence_cipher_encrypt.py](https://github.com/djotaku/impracticalpython/blob/master/Ch04/Project%209%20-%20The%20Rail%20Fence%20Cipher/rail_fence_cipher_encrypt.py)
- to get every other item in a list (or every other letter in a string):
```python
iterable[::2]  # would get every other item starting with 0
iterable[1::2] # gets every other item starting with 1
```
- itertools.zip_longest() allows you to zip (or combine) two iterators of unequal length. It just appends None where the shorter string falls short.
