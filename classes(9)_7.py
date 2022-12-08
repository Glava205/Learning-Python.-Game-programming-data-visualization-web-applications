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
		super().__init__(first_name,last_name,user_name)
		self.privileges=[]
	def show_privileges(self):
		for privelege in self.privileges:
			print("Admin "+privelege)

my_profile=Admin("vlad","golovchits","glava205")
my_profile.privileges=[' can add post',' can delete post',' can ban user']
my_profile.show_privileges()
