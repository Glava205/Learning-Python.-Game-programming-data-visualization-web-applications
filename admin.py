from user_class import User

class Admin(User):
	def __init__(self,first_name,last_name,user_name):
		self.privileges=Privileges()


class Privileges(Admin):
	def __init__(self,privileges=[]):
		self.privileges=privileges
	
	def show_privileges(self):
		for privelege in self.privileges:
			print("Admin"+privelege)
