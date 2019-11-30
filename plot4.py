from matplotlib import pyplot as plt

x = [1, 3, 5, 7, 9]
y = [5, 2, 7, 8, 2]
x1 = [2, 4, 6, 8, 10]
y1= [8, 6, 2 ,5, 6]

plt.bar(x, y, label = "Bar 1")
plt.bar(x1, y1, label = "Bar 2", color = 'g')

plt.legend()

plt.title("Bar Graph")
plt.ylabel("Bar Height")
plt.xlabel("Bar Number")

plt.show()