my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]

my_foods.append('cannoli')
my_foods.append('potato')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("The first three items in the list are:")
print(my_foods[0:3])

print("Three items from the middle of the list are:")
print(my_foods[1:-1])

print("The last three items in the list are:")
print(my_foods[-3:])
