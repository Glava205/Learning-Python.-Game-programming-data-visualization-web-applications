from random import randint

class Die ():
	
	def __init__(self,sides=6):
		self.sides=sides
	
	def roll_die(self):
		i=1
		while i<=10:
			self.x=randint(1,self.sides)
			print(self.x)
			i+=1

die=Die(20)
die.roll_die()
