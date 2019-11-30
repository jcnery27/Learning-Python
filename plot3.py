from matplotlib import pyplot as plt
from matplotlib import style

style.use("ggplot")

x = [5, 8, 10]
y = [12, 16, 6]
x1 = [6, 9, 11]
y1 = [6, 15, 7]

plt.plot(x, y, 'g', label = 'Line 1', linewidth = 10)
plt.plot(x1, y1, 'b', label = 'Line 2', linewidth = 5)
plt.legend()
plt.title("Epic Information")
plt.ylabel("Y-Axis")
plt.xlabel("X-Axis")

plt.show()