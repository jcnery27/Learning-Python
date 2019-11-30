from matplotlib import pyplot as plt

x = [7, 2, 2, 13]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'b']

plt.pie(x,
	labels = activities,
	colors = cols,
	startangle = 90,
	shadow = True,
	explode = (0.99, 0.99 ,0.99 ,0.99),
	autopct = '%1.3f%%')

plt.title("Pie Chart")
plt.show()