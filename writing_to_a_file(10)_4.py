filename='guest_book.txt'

with open(filename,'a') as file_object:
	while True:
		print("What is your name?")
		print("If you want to quit write 'q'")
		name=input()
		if name=='q':
			break
		else:
			file_object.write("Hello, "+str(name.title())+"!\n")
