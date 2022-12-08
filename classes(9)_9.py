class Car():
	def __init__(self,make,model,year):
		self.make=make
		self.model=model
		self.year=year
		self.odometr_reading=0
	
	def get_descriptive_name(self):
		long_name=str(self.year)+' '+self.make+' ' +self.model
		return long_name.title()
	
	def read_odometr(self):
		print("This car has "+str(self.odometr_reading)+ " miles on it")
	
	def update_odometr(self,mileage):
		if mileage>=self.odometr_reading:
			self.odometr_reading=mileage
		else:
			print("You can't roll back on odometr!")
	
	def increment_odometr(self,miles):
		self.odometr_reading+=miles

class Battery():
	
	def __init__(self,battery_size=70):
		self.battery_size=battery_size
	
	def describe_battery(self):
		print("This car has a "+str(self.battery_size)+"-kWh battery.")
		
	def get_range(self):
		if self.battery_size==70:
			range=240
		elif self.battery_size==85:
			range=270
		message="This car go approximately "+str(range)
		message+=" miles on a full charge."
		print(message)
	
	def upgrade_batery(self):
		if self.battery_size!=85:
			self.battery_size=85

class ElectricCar(Car):
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.battery=Battery()
	
	def fill_gas_tank():
		print("This car doesn't need a gas tank!")


my_tesla=ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_batery()
my_tesla.battery.get_range()
