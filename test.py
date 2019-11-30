class Baby():
	name = "Biebs"
	age = "15"
	gender = "F"
	def _init_(self):
		self.name = ""
		self.age = ""
		self.gender = ""

	def talk(self):
		print("Baby, Baby, Baby, Ooh!")

	def getName(self):
		return self.name

	def setName(self, temp):
		self.name = temp

	def getAge(self):
		return self.age

	def setAge(self, temp):
		self.age = temp

	def getGender(self):
		return self.gender

	def setGender(self, temp):
		self.gender = temp

justin = Baby()
justin.talk()
justin.setName("Justin")
justin.setGender("M")
justin.setAge(16)

bieber = Baby()

print(justin.getName(), justin.getAge(), justin.getGender())
print(bieber.getName(), bieber.getAge(), bieber.getGender())