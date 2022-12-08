famous_person_0={'first':'Stas','last':'Asafev','age':30,'city':'Moscow'}
famous_person_1={'first':'ilon','last':'mask','age':35,'city':'san-francisko'}
famous_person_2={'first':'adolf','last':'gitler','age':50,'city':'berlin'}

people=[famous_person_0,famous_person_1,famous_person_2]

for person in people:
	print(person['first'].title()+" "+ person['last'].title()+", age "+str(person['age']) + ", live in " + person['city'].title())

