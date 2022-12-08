guests=['Elon Musk','Stas Asafev','morgenshtern']



message="Dear "+guests[0].title()+", I invite you to lunch!"
print(message)

message="Dear "+guests[1].title()+", I invite you to lunch!"
print(message)

message="Dear "+guests[2].title()+", I invite you to lunch!"
print(message)



popped_guest=guests.pop(1)
print(popped_guest)

guests.append('Jaromir jagr')



message="Dear "+guests[0].title()+", I invite you to lunch!"
print(message)

message="Dear "+guests[1].title()+", I invite you to lunch!"
print(message)

message="Dear "+guests[2].title()+", I invite you to lunch!"
print(message)



print('I rent a big lunch table')

guests.insert(0,'Bill geyts')
guests.insert(2,'Dasha')
guests.append('Maksim')

print(guests)

print("\n")



message="Dear "+guests[0].title()+", I invite you to lunch!"
print(message)

message="Dear "+guests[1].title()+", I invite you to lunch!"
print(message)

message="Dear "+guests[2].title()+", I invite you to lunch!"
print(message)

message="Dear "+guests[3].title()+", I invite you to lunch!"
print(message)

message="Dear "+guests[4].title()+", I invite you to lunch!"
print(message)

message="Dear "+guests[5].title()+", I invite you to lunch!"
print(message)



print("I invite only 2 guests to lunch")

popped_guest=guests.pop(5)
print("I'm sorry, dear "+popped_guest.title())

popped_guest=guests.pop(4)
print("I'm sorry, dear "+popped_guest.title())

popped_guest=guests.pop(3)
print("I'm sorry, dear "+popped_guest.title())

popped_guest=guests.pop(2)
print("I'm sorry, dear "+popped_guest.title())



message="Dear "+guests[0].title()+", I invite you to lunch!"
print(message)

message="Dear "+guests[1].title()+", I invite you to lunch!"
print(message)



del guests[1]
del guests[0]

print(guests)
