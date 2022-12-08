class User():
	def __init__(self,first_name,last_name,user_name):
		self.first_name=first_name
		self.last_name=last_name
		self.user_name=user_name
		self.login_attempts=0
	
	def describe_user(self):
		print(self.user_name+" "+self.first_name.title()+" "+self.last_name.title())
	
	def greet_user(self):
		print("\nHello "+self.user_name+"!")
	
	def increment_login_attempts(self):
		self.login_attempts+=1
	
	def reset_login_attempts(self):
		self.login_attempts=0

my_profile=User('vlad','golovchits','glava205')
dad_profile=User('vadim','golovchits','vadisha')

my_profile.greet_user()
my_profile.describe_user()

dad_profile.greet_user()
dad_profile.describe_user()

my_profile.increment_login_attempts()
my_profile.increment_login_attempts()

print(my_profile.login_attempts)

my_profile.reset_login_attempts()

print(my_profile.login_attempts)
