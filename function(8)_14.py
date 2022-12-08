def make_car(manufacturer,model,**others):
	car_info={}
	car_info['manufacturer']=manufacturer
	car_info['model']=model
	for key,value in others.items():
		car_info[key]=value
	return car_info

car=make_car('subaru','outback',color='blue',tow_peckage=True)
print(car)

