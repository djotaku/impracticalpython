# What I learned

# Genetic Algorithms
- Eventually optimizations bottom out

# Crackign a High-Tech Safe
- a combination lock should be called a permutation lock because it requires ordered combinations. But there can also be repetitions.

# Python

- awareness of the statistics module
    - statitics.mean - no need to do it manually again!
- existence of the random.triangular function. Not a big stats person, so the fact that it does a triangular distribution means nothing to me, but if I come across a problem that needs it, now I know that it exists.
- random.shuffle(iterable?). I'd heard of random.choice() before, but not random.shuffle().
- random.randint(lower, higher) - you don't need to use higher+1 - it uses all the numbers
- random.uniform(min, max) to get a uniform distribution and pick a random number from that distribution
- a reminder that zip(iterable, iterable) exists and can be very useful
- itertools permutations can't help in the safe cracking because it returns permutations with without repetition. So you need to use itertools product(). That calculates the Cartesian product from multiple sets of numbers. 

# Random
- I guess computer power has increased a lot since the book was published. The author says the rat algorithm will take 2 seconds and it took me .11 seconds.
