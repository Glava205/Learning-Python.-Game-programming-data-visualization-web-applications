line = "Hello"
print(line=="Hello")
print(line=="Bye")

car = "Audi"
print(car.lower()=="audi")
print(car.lower()=="Audi")

number=10
print(number>5)
print(number>20)
print(number<20)
print(number<5)
print(number>=10)
print(number>=11)
print(number<=11)
print(number<=3)

print( (number>5) and (number<20))
print( (number>11) and (number>5))
print( (number>11) or (number>5))
print( (number>11) or (number<5))

cars=['audi','bmw','subaru','toyota']
print('audi'in cars)
print('BMW' in cars)

print('BMW' not in cars)
print('audi' not in cars)
