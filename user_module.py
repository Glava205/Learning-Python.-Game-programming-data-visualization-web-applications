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

class Admin(User):
	def __init__(self,first_name,last_name,user_name):
		self.privileges=Privileges()


class Privileges(Admin):
	def __init__(self,privileges=[]):
		self.privileges=privileges
	
	def show_privileges(self):
		for privelege in self.privileges:
			print("Admin"+privelege)
