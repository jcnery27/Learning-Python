from sys import argv

x, P, Y, R = argv

P = float(P)
Y = int(Y)
R = float(R)

n = 12 * Y
r = R/(12*100)

payment = (P*r)/(1-(1+r)**-n)
print(payment)