import json

f_num=input("What is your favorite number? ")
filename='favorite_number.txt'

with open(filename,'w') as f_obj:
	json.dump(f_num,f_obj)

with open(filename) as f_obj:
	out=json.load(f_obj)
	print("I know your favorite number! It is "+out)
