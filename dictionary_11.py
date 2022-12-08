cities={
	'minsk':{'country':'belarus','popuation':'2 mln','fact':'Вероятнее всего, своим названием Минск обязан речке Мене, что означает «мелкая» или «меньшая».'},
	'moscow':{'country':'russia','population':'12 mln','fact':'Площадь Москвы примерно такая же, как у Нью-Йорка.'},
	'kiev':{'country':'ukrain','population':'3 mln','fact':'Согласно легенде, Киев был назван в честь Кия – одного из трех братьев, основавших город.'},
	}

for city,info in cities.items():
	print(city.title())
	for k,v in info.items():
		print(k.title() + " " + str(v).title())
	print("\n")
