prompt="Write your age:"
prompt+="\nIf you want to get out, write 'quit'"
message=input(prompt)

while message!='quit':
	age = int(message)
	if age<3:
		print("You don't have to pay for admission")
	elif age>=3 and age<=12:
		print("You need to pay for admission 10$")
	elif age>12:
		print("You need to pay for admission 15$")
	message=input(prompt)
