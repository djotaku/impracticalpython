"""A genetic algorithm to solve break a combination lock for 007"""

###############################################
# Scenario:
# James Bond has to quickly crack a safe. 
# Assumes use of a sound amplifying tool, 
# along with a tool to prevent lockouts
# after a few incorrect combinations. 
# The sound tool can only tell you *how many*
# digits are correct, not *which* digits.
################################################

import time
from random import randint, randrange

def fitness(combo, attempt):
    """Compare items in 2 lists and count number of matches."""
    grade = 0
    for i, j in zip(combo, attempt):
        if i == j:  # you are not recording the index, because of scenario description above
            grade += 1
    return grade

def main():
    """Use hill-climbing algorithm to solve lock combination."""
    combination = '6822858902'
    print(f"Combination = {combination}")
    # convert combination to list:
    combo = [int(i) for i in combination]
    
    # generate guess & grade fitness
    best_attempt = [0] * len(combo)
    best_attempt_grade = fitness(combo, best_attempt)
    
    count = 0
    
    # evolve guess
    while best_attempt != combo:
        # crossover
        next_try = best_attempt[:]
        
        # mutate
        lock_wheel = int(randrange(0, len(combo)))
        next_try[lock_wheel] = randint(0, len(combo)-1)
        
        # grade and select
        next_try_grade = fitness(combo, next_try)
        if next_try_grade > best_attempt_grade:
            best_attempt = next_try[:]
            best_attempt_grade = next_try_grade
        print(next_try, best_attempt)
        count += 1
    
    print()
    print(f"Cracked! {best_attempt} in {count} tries!")


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print(f"\nRuntime for this program was {duration:.5f} seconds.")
