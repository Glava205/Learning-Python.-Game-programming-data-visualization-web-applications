vacations={}

flag=True

while flag:
	name=input("\nWhat is our name?")
	vacation=input("Where would you like to go on vacation?")
	vacations[name]=vacation
	out=input("Would you like to go exit?(yes/no)")
	if out=='yes':
		flag=False

for name,vacation in vacations.items():
	print(name.title()+" would like to go to "+vacation.title())
