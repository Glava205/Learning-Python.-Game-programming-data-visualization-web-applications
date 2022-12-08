available_toppings=['mushrooms','olives','green peppers','pepperoni','pineapple','extra chesse']

requested_toppings=['mushrooms','french fries','extra chesse']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding "+requested_topping+".")
	else:
		print("Sorry, we don't have "+requested_topping+".")

print("\nFinished making your pizza!")

