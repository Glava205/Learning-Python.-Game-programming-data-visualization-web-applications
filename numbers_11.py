pizzes=['barbecue','chesses','salami']
for pizza in pizzes:
	print("I like "+pizza+" pizza.")
	print("\n")
print("I really love pizza!")

friend_pizzas=pizzes[:]

pizzes.append('chiken')
friend_pizzas.append('karbonad')

print("My favorite pizzas are:")
print(pizzes)

print("My friend's favorite pizzas are:")
print(friend_pizzas)
