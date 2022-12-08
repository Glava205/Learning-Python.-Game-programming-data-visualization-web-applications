try:
	filename='cats.txt'
	
	with open(filename,'a+') as f_obj:
		f_obj.write("Белочка\n")
		f_obj.write("Арабика\n")
		f_obj.write("Пинки\n")
		contents=f_obj.readlines()
		print(contents)
		
	filename='dogs.txt'
	
	with open(filename,'a+') as f_obj:
		f_obj.write("Дарман\n")
		f_obj.write("Цезарь\n")
		f_obj.write("Одиссей\n")
		print(f_obj.read())

except FileNotFoundError:
	print("File not found in your directory")
