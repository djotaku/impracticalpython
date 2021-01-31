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

import sys
import time
from random import randint, randrange, choice

def fitness(combo, attempt):
    """Compare items in 2 lists and count number of matches."""
    grade = 0
    correct_indices = []
    comparison = zip(combo, attempt)
    for index, (i, j) in enumerate(comparison):
        if i == j:
            grade += 1
            correct_indices.append(index)
    return grade, correct_indices

def main():
    """Use hill-climbing algorithm to solve lock combination."""
    combination = '6822858902'
    print(f"Combination = {combination}")
    # convert combination to list:
    combo = [int(i) for i in combination]
    
    safe_indices = []
    
    # generate guess & grade fitness
    best_attempt = [0] * len(combo)
    best_attempt_grade, safe_indices = fitness(combo, best_attempt)
    
    count = 0
    lock_wheels = [number for number in range(0, len(combo))]
    
    # evolve guess
    while best_attempt != combo:
        # crossover
        next_try = best_attempt[:]
        
        # mutate
        lock_wheel = choice(lock_wheels)
        next_try[lock_wheel] = randint(0, len(combo)-1)
        
        # grade and select
        next_try_grade, safe_indices = fitness(combo, next_try)
        if next_try_grade > best_attempt_grade:
            best_attempt = next_try[:]
            best_attempt_grade = next_try_grade
            for safe_index, lock_wheel in zip(safe_indices, lock_wheels):
                if safe_index == lock_wheel:
                    lock_wheels.remove(lock_wheel)
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
