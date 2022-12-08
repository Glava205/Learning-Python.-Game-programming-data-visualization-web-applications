#Создание пустого списка для хранения пришельцев.
aliens=[]
#Сщздание 30 зеленых пришельцев
for alein_number in range(30):
	new_alien={'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)

for alien in aliens[0:3]:
	if alien['color']=='green':
		alien['color']='yellow'
		alien['speed']='medium'
		alien['points']=10
	elif alien['color']=='yellow':
		alien['color']='red'
		alien['speed']='fast'
		alien['points']=15

#вывод первых 5 пришельцев:
for alien in aliens[:5]:
	print(alien)
print("...")

#Вывод количества созданных пришельцев.
print("Total number of aliens: " + str(len(aliens)))
