import json 


def get_stored_number():
	"""получает хранимое имя пользователя если оно существует"""
	filename='favorite_number.txt'
	
	try:
		with open(filename) as f_obj:
			out=json.load(f_obj)
	except FileNotFoundError:
		return None


def get_new_number():
	"""запрашивает новое имя пользователя"""
	number=input("What is your favorite number?")
	filename='favorite_number.txt'
	with open(filename,'w') as f_obj:
		json.dump(number,f_obj)
	return number


def favorite_number():
	"""приветствует пользователя по имени"""
	number=get_stored_number()
	if number:
		print("I know your favorite number!It is "+str(number))
	else:
		numbere=get_new_number()
		print("We'll remember you favorite number when you come back, "+str(number)+"!")

favorite_number()
