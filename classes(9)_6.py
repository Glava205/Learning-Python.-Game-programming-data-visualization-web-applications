class Restaurant():
	
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
		self.number_served=0
	
	def describe_restaurant(self):
		print(self.restaurant_name.title())
		print(self.cuisine_type.title())
	
	def open_restaurant(self):
		print(self.restaurant_name.title()+" is open.")
	
	def set_number_served(self,served):
		self.number_served=served
		print(self.number_served)
	
	def increment_number_served(self,serv):
		self.number_served+=serv
		print(self.number_served)

class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name,cuisine_type):
		super().__init__(restaurant_name,cuisine_type)
		self.flavors=['Butter Pecan','Chocolate chip cookie dough','Chocolate']
	
	def describe_flavor(self):
		for flavor in self.flavors:
			print("We have "+flavor+".")

ice_cream=IceCreamStand("Bubble","european")
ice_cream.describe_flavor()

