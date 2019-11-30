name1 = input("Enter your name: ")
name2 =  input("Enter your crush's name: ")
flames = {"F": "Friendship", "L": "Love", "A": "Affection", "M": "Marriage", "E": "Enemy", "S": "Soulmate"}

for x in name1:
	for y in name2:
		name1.strip(y)
		name2.strip(y)
