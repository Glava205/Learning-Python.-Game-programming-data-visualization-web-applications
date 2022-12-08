try:
	first_number=input()
	second_number=input()
	print(int(first_number)+int(second_number))
except ValueError:
	print("You write non numeracal symbol")
