- an example of an even more complex way to print with the splat operator -> print("Anagrams =", *anagram_list, sep='\n') leads to the following output:

```
Anagrams
forest
fortes
softer
```

- how to make use of collections.Counter. It takes in an iterable and stores the items ad dictionary keys and the coutns as dictionary values. eg:

```python

>>> from collections import Counter
>>> my_bonsai_trees = ['maple', 'oak', 'elm', 'maple', 'elm', 'elm', 'elm', 'elm']
>>> count = Counter(my_bonsai_trees)
>>> print(count)
Counter({'elm': 5, 'maple': 2, 'oak': 1})
```

If you use it on a word, then it will use the letters as the items and how many times those letters appear as numbers.

- variable_name = input("some text") will display that text to the user and then store input.


