rivers={'neman':'lithuania','volga':'russia','amazonka':'brazilia'}

for river in rivers.keys():
	print("The "+river.title()+" runs through "+rivers[river].title()+'.')

print("\n")

for river in rivers.keys():
	print(river.title())

print("\n")

for country in rivers.values():
	print(country.title())
