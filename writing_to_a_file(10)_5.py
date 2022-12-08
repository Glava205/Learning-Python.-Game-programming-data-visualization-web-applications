filename='question.txt'

with open(filename,'a') as file_object:
	while True:
		print("Why do you like programming?")
		print("If you want to quit write 'q'")
		answer=input()
		if answer=='q':
			break
		else:
			file_object.write(answer+"\n")
