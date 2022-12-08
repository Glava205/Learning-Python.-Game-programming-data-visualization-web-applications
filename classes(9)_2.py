class Restaurant():
	
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
	
	def describe_restaurant(self):
		print("\n"+self.restaurant_name.title())
		print(self.cuisine_type.title())
	
	def open_restaurant(self):
		print(self.restaurant_name.title()+" is open.")

elion=Restaurant('Elion','chinish')

elion.describe_restaurant()
elion.open_restaurant()

ovion=Restaurant('ovion','europian')
ovion.describe_restaurant()

coctail_bar_duck=Restaurant('coctail bar duck','europian')
coctail_bar_duck.describe_restaurant()

