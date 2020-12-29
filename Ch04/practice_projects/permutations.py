"""Return a collection of tuples of all possible permutations for cipher keys."""

from itertools import permutations, product

def key_permutations(columns):
    values_for_key = [number for number in range(1, columns+1)]
    return_values = []
    for permutation in permutations(values_for_key):
        for signs in product([-1,1], repeat=len(values_for_key)):
            return_values.append([number*sign for number, sign in zip(permutation, signs)])
    return return_values

def main():
    columns = int(input("How many columns will your route cipher have? "))
    print(list(key_permutations(columns)))


if __name__ == "__main__":
    main()
