"""Find all word-pair palingrams in a dictionary file."""
import load_dictionary

word_list = load_dictionary.load('words.txt')

# find word-pair palingrams
def find_palingrams():
    """Find dictionary palingrams.
    
    Optimized by using sets instead of lists."""
    pali_list = []
    words = set(word_list)
    for word in words:
        end = len(word)
        rev_word = word[::-1] # alternatively use ''.join(reversed(word))
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in words:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in words:
                    pali_list.append((rev_word[:end-i], word))
    return pali_list

palingrams = find_palingrams()

# sort palingrams on first word
palingrams_sorted = sorted(palingrams)

# display list of palingrams
print(f"\nNmber of palingrams = {len(palingrams_sorted)}")
for first, second in palingrams_sorted:
    print(f"{first} {second}")
