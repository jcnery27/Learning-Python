interval = int(input("Enter a value: "))

if interval == -50 or interval == 50 or interval == 0:
	print ("Border")
elif interval < 0 and interval > -50:
	print ("Negative Range")
elif interval > 0 and interval < 50:
	print ("Positive Range")
else :
	print("Out of Range")
