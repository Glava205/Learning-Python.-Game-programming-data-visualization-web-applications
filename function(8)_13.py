def build_profile(first,last,**user_info):
	profile={}
	profile['first_name']=first
	profile['last_name']=last
	for key,value in user_info.items():
		profile[key]=value
	return profile

user_profile=build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)

my_profile=build_profile('vlad','golovchits',location='minsk',study='bsuir',hobby='hockey')
print(my_profile)
