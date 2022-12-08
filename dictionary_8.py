tesla={'animal_type':'dog','owner':'vlad'}
bona={'animal_type':'cat','owner':'ala'}

pets=[tesla,bona]

for pet in pets:
	print(str(pet).title())
	print(pet['animal_type'].title()+"-"+pet['owner'].title())


