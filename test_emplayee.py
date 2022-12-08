from unittest import main, TestCase
from employee import Employee
 
class TestEmployee(TestCase):
    def setUp(self):
        self.employee = Employee('John', 'Smith', 3500)
 
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(8500, self.employee.salary)
 
    def test_give_custom_raise(self):
        self.employee.give_raise(500)
        self.assertEqual(4000, self.employee.salary)
 
 
if __name__ == '__main__':
    main()
