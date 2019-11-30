from matplotlib import pyplot as plt
import numpy as np

population_ages = np.random.randint(1, 100, 99)
bins = range(0, 101, 10)

plt.hist(population_ages, bins, histtype = 'bar', width = 8)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Histogram")
plt.legend()
plt.show()