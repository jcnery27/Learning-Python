#imports
import math

#inputs
a = int(input("Enter value: "))
b = int(input("Enter value: "))
c = int(input("Enter value: "))

#processes
s = (a + b + c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))

#output
print(area)