names_numbers={
	'nazar':[12,99],
	'vlad':[3,11],
	'andrey':[10,23],
	'ivan':[57,7],
	'kirill':[6,96]
	}

for name,numbers in names_numbers.items():
	print(name.title())
	for number in numbers:
		print(number)
	print("\n")
