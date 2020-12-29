"""Return a collection of tuples of all possible permutations for cipher keys."""

from itertools import combinations

def key_permutations(columns):
    values_for_key = []
    for number in range(-columns, columns):
        if number != 0:
            values_for_key.append(number)
    return permutations(values_for_key, r=columns)

def main():
    columns = int(input("How many columns will your route cipher have? "))
    print(list(key_permutations(columns)))


if __name__ == "__main__":
    main()
