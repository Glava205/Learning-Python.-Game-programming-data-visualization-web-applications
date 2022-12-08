names=['Brenda','Ricky','William','admin','Maria']

for name in names:
	if name=='admin':
		print("Hello admin, would you like to see a status report?")
	else:
		print("Hello "+name.title()+", thank you for logging again")
