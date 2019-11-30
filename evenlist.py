x_list = [11, 6, 5, 7, 10]
#i = 0
print("The original list was: ",x_list)

for a in range(len(x_list)):
	if x_list[a]%2 == 0:
		#a = a + 1
		x_list[a] = x_list[a] + 1
	#i = i + 1

print("The new list is: ", x_list)