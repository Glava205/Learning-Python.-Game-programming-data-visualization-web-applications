filename='learning_python.txt'

with open(filename) as file_object:
	learning=file_object.readlines()

for line in learning:
	print(line)

