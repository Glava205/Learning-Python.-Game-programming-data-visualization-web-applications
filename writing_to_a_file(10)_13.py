import json 


def get_stored_username():
	"""получает хранимое имя пользователя если оно существует"""
	filename='username.json'
	
	try:
		with open(filename) as f_obj:
			username=json.load(f_obj)
	except FileNotFoundError:
		return None


def get_new_username():
	"""запрашивает новое имя пользователя"""
	username=input("What is your name?")
	filename='username.json'
	with open(filename,'w') as f_obj:
		json.dump(username,f_obj)
	return username



def greet_user():
	"""приветствует пользователя по имени"""
	username=get_stored_username()
	while True:	
		answer=input("Your name is "+str(username)+"?(Y/N)")
		if answer=='Y':
			print("Welcome back, "+str(username)+"!")
			break
		elif answer=='N':
			username=get_new_username()
			print("We'll remember you when you come back, "+str(username)+"!")
			break
		else:
			print("You must write 'Y' or 'N'")
			continue


greet_user()

