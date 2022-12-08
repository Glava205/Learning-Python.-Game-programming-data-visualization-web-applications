def make_album(name,album_name,number_of_tracks=''):
	album={album_name:[name,number_of_tracks],}
	print(album)

counter=0
while counter<3:
	name=input("\nWrite name executor ")
	album_name=input("\nWrite name album ")
	number_of_tracks=input("\nWrite number of tracks ")
	make_album(name,album_name,number_of_tracks)
	counter+=1
