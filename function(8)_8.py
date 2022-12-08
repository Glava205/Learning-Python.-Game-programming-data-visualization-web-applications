def make_album(name,album_name,number_of_tracks=''):
	album={album_name:[name,number_of_tracks],}
	print(album)


while True:
	print("(enter 'q' at any time to quit)")
	name=input("\nWrite name executor ")
	if name=='q':
		break
	album_name=input("\nWrite name album ")
	if album_name=='q':
		break
	number_of_tracks=input("\nWrite number of tracks ")
	if number_of_tracks=='q':
		break
	make_album(name,album_name,number_of_tracks)
