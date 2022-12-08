curret_users=['Jack','Dorothy','Courtney','John','Melanie']

new_users=['Edward','Margaret','Mary','Melanie','Regina']

for new_user in new_users:
	for curret_user in curret_users:
		if new_user.upper() in curret_user.upper():
			tf=False
		else:
			tf=True
	if tf==True:
		print("Correct name")
	else:
		print("You should choose a different name")
