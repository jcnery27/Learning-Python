import numpy as np
from matplotlib import pyplot as plt

def f(t):
	return np.exp(-t)*np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.2)

plt.subplot(221)
plt.plot(t1, f(t1), 'bo', t2, f(t2))

plt.subplot(122)
plt.plot(t2, np.cos(2*np.pi*t2))

plt.show()  