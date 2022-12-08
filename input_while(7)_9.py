sandwich_orders=['Classic English sandwich','pastrami','Ham and cheese sandwich','pastrami','Club Sandwich','pastrami']
finished_sandwiches=[]

print(sandwich_orders)

for sandwich in sandwich_orders:
	print("I made your "+sandwich+".")
	finished_sandwiches.append(sandwich)

print("Pastrami is no more")

while 'pastrami' in finished_sandwiches:
	finished_sandwiches.remove('pastrami')

print(finished_sandwiches)
