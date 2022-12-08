def show_magicians(magicians):
	for magician in magicians:
		print(magician)

def make_great(magicians):
	great_magicians=[]
	while magicians:
		magician=magicians.pop()
		great_magicians.append("Great "+magician)
	magicians=great_magicians
	print(magicians)

magicians=['Гарри Гудини','Дэвид Копперфильд','Дэвид Блейн']
show_magicians(magicians)
make_great(magicians)
