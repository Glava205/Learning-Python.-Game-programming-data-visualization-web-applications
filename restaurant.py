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


