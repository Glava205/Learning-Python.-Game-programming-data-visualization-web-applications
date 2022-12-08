additions=""
prompt="Write a pizza supplement:"
prompt+="\nIf you want to get out, write 'quit'"

while additions!='quit':
	additions=input(prompt)
	if additions=='quit':
		break
	print(additions.title()+" added!")

