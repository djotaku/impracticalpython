"""Simulate breeding rats to get them to the size (weight) of a female bullmastiff."""

import time
import random
import statistics

# CONSTANTS (weights in grams)
GOAL = 50000  # target weight in grams (female bullmastiff)
NUM_RATS = 20  # totla nubmer of adult rats your lab can support
INITIAL_MIN_WT = 200  # minimum weight of adult rat, in grams, in initial population
INITIAL_MAX_WT = 600  # maximum weight of adult rat, in grams, in initial population
INITIAL_MODE_WT = 300  # most common adult rat weight, in grams, in initial population
MUTATE_ODDS = 0.01  # Probability of a mutation occurring in a rat
MUTATE_MIN = 0.5  # Scalar on rat weight of least beneficial mutation
MUTATE_MAX = 1.2  # Scalar on rat weight of most beneficial mutation
LITTER_SIZE = 8  # Number of pups per pair of mating rats
LITTERS_PER_YEAR = 10  # Number of litters per year per pair of mating rats
GENERATION_LIMIT = 500  # Generational cutoff to stop breeding program

# ensure even-number of rats for breeding pairs:
if NUM_RATS % 2 != 0:
    NUM_RATS += 1


def populate(num_rats, min_wt, max_wt, mode_wt):
    """Initialize a population with a triangular distribution of weights."""
    return [int(random.triangular(min_wt, max_wt, mode_wt)) for i in range(num_rats)]


def fitness(population, goal):
    """Measure population fitness based on an attribute mean vs target."""
    ave = statistics.mean(population)
    return ave / goal  # when this values is >= 1, you'll know it's time to stop breeding


def selection(population, to_retain):
    """Cull a population to retain only a specified number of members.
    
    :param population: The parents of each generation.
    "param to_retain: bring us down to the NUM_RATS value.
    """
    sorted_population = sorted(population)
    to_retain_by_sex = to_retain // 2  # floor division to split the number of rats to retain in half
    members_per_sex = len(sorted_population)//2  # we want to take the parents and divide in half to count males and females
    females = sorted_population[:members_per_sex]  # since males are larger than females, assume the first half of the sorted list is femailes
    males = sorted_population[members_per_sex:]  #  accordingly, the second half of the list should be males
    selected_females = females[-to_retain_by_sex:]  # use negative slicing to grab the back half of the list - the largest females
    selected_males = males[-to_retain_by_sex:]  # use negative slicing to grab the back half of the list - the largest males
    return selected_males, selected_females


def breed(males, females, litter_size):
    """Crossover genes among members (weights) of a population."""
    random.shuffle(males)  # because we sorted them previously and don't want to end up pairing smallest with smallest
    random.shuffle(females)  # because we sorted them previously and don't want to end up pairing smallest with smallest
    children = []
    for male, female in zip(males, females):
        for child in range(litter_size):
            child = random.randint(female, male)  # baby should have a size somewhere between mom and dad
            children.append(child)
    return children


def mutate(children, mutate_odds, mutate_min, mutate_max):
    """Randomly alter rat weights using input odds and fractional changes."""
    for index, rat in enumerate(children):
        if mutate_odds >= random.random():
            children[index] = round(rat * random.uniform(mutate_min, mutate_max))  # pick a random number from a uniform distribution
    return children


def main():
    """Initialize population, select, breed, and mutuate; display results."""
    generations = 0
    parents = populate(NUM_RATS, INITIAL_MIN_WT, INITIAL_MAX_WT, INITIAL_MODE_WT)
    print(f"initial population weights = {parents}")
    popl_fitness = fitness(parents, GOAL)
    print(f"Initial population fitness = {popl_fitness}")
    print(f"Number to retain = {NUM_RATS}")
    
    ave_wt = []
    
    while popl_fitness < 1 and generations < GENERATION_LIMIT:
        selected_males, selected_females = selection(parents, NUM_RATS)
        children = breed(selected_males, selected_females, LITTER_SIZE)
        children = mutate(children, MUTATE_ODDS, MUTATE_MIN, MUTATE_MAX)
        parents = selected_males + selected_females + children
        popl_fitness = fitness(parents, GOAL)
        print(f"Generation {generations} fitness = {popl_fitness:4f}")
        ave_wt.append(int(statistics.mean(parents)))
        generations += 1
    print(f"average weight per generation = {ave_wt}")
    print(f"\nnumber of generations = {generations}")
    print(f"number of years = {int(generations/LITTERS_PER_YEAR)}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print(f"\nRuntime for this program was {duration} seconds.")
