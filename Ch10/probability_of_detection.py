from random import randint
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

NUM_EQUIV_VOLUMES = 1000  # number of locations in which to place civilizations
MAX_CIVS = 5000  # maximum number of advanced civilizations
TRIALS = 1000  # number of times to model a given number of cilizations
CIV_STEP_SIZE = 100  # civilizations count step size 

x = []  # x values for polynomial fit
y = []  # y values for polynomial fit

for num_civs in range(2, MAX_CIVS + 2, CIV_STEP_SIZE):  # number of civs to model
    civs_per_vol = num_civs / NUM_EQUIV_VOLUMES
    num_single_civs = 0  # number of locations contianing a single civilization
    for trial in range(TRIALS):  # for each trial distribute same number of civs
        locations = []  # equivalent volumes containing a civilization
        while len(locations) < num_civs:  # pick loc at random and append to list
            location = randint(1, NUM_EQUIV_VOLUMES)
            locations.append(location)
        overlap_count = Counter(locations)
        overlap_rolloup = Counter(overlap_count.values())
        num_single_civs += overlap_rolloup[1]

    prob = 1 - (num_single_civs / (num_civs * TRIALS))

    # print ratio of civs-per-volume vs probability of 2+ civs per locations
    # print("{:.4f} {:.4f}".format(civs_per_vol, prob))  # comment out to speed things up.
    x.append(civs_per_vol)
    y.append(prob)


coefficients = np.polyfit(x, y, 4)  # 4th order polynomial fit
p = np.poly1d(coefficients)
print(f"\n{p}")
xp = np.linspace(0, 5)
_ = plt.plot(x, y, '.', xp, p(xp), '-')
plt.ylim(-0.5, 1.5)
plt.show()
