from operator import itemgetter
productList = ["Sensodyne-100, Close Up-150, Colgate-135", "Safeguard-80, Protex-50, Kojic-135","Surf-280, Ariel-350, Tide-635", "Clover-60, Piatos-20, Chippy-35", "Jelly bean-60, Hany-20, Starr-35"]
categories = []
total = 0.0
cheapestItems = ""
for a in productList:
	categories.append(a.split(", "))
for products in categories:
	items = []
	for product in products:
		y = product.split("-")
		items.append([y[0],float(y[1])])
	items = sorted(items, key =itemgetter(1), reverse = False)
	total += float(items[0][1])
	cheapestItems += items[0][0] + " - " + str(items[0][1]) + ", "
print("Cheapest Items: " + cheapestItems[0:-2])
print("Total: ",  total)