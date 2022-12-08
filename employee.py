class Employee():
    def __init__(self, name, second_name, salary):
        self.name = name
        self.second_name = second_name
        self.salary = salary
 
    def give_raise(self, amount=5000):
        self.salary += amount
 
