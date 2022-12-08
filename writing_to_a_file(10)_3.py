guest_name=input("What is your name? ")

filename='guest.txt'

with open(filename,'a') as file_object:
	file_object.write(guest_name)
