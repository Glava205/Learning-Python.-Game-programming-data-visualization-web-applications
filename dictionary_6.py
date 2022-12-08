names=['maksim','jen','nazar','phill']

favorite_languages={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}

for name in names:
	if name in favorite_languages.keys():
		print("Thanks "+ name.title()+ " for taking the survey.")
	elif name not in favorite_languages.keys():
		print(name.title()+", don't want to take the survey")

