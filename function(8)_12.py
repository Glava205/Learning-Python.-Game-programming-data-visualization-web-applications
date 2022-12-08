def make_sandwich(*toppings):
	print("\nSandwich consists of:")
	for topping in toppings:
		print("- "+ topping)

make_sandwich('bread','meat')
make_sandwich('bread','meat','cucumber','tomato')
make_sandwich('bread')

