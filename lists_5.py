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
