def show_magicians(magicians):
	for magician in magicians:
		print(magician)

def make_great(magicians,great_magicians):
	great_magicians=[]
	while magicians:
		magician=magicians.pop()
		great_magicians.append("Great "+magician)
	print(great_magicians)

magicians=['Гарри Гудини','Дэвид Копперфильд','Дэвид Блейн']
great_magicians=[]
show_magicians(magicians)
make_great(magicians[:],great_magicians)
show_magicians(great_magicians)
show_magicians(magicians)

