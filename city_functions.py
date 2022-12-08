def city_country(city,country,population=''):
	if population:
		out=city.title()+', '+country.title()+"- population "+population+'.'
	else:
		out=city.title()+', '+country.title()
	return out

