favorite_places={
	'nazar':['minsk','moscow'],
	'ala':['warsawa','belostok'],
	'vadim':['geneva','berlin'],
}

for name,places in favorite_places.items():
	print(name.title())
	for place in places:
		print(place.title())
	print("\n")
