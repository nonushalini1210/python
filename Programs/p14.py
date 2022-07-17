#python object-oriented programming
class Employee:
 
    num_of_emps= 0
    raise_amt= 1.04

    def __init__(self, first, last, pay):
         self.first= first
         self.last= last
         self.pay= pay
         self.email= first+'.' + last + '@company.com'
         self.pay= pay

         Employee.num_of_emps +=1

    def fullname(self):
        return'{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay= int(self.pay * self.raise_amt)
        
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday()== 5 or day.weekday() == 6:
            return False
        return True

emp_1= Employee('Corey', 'Schafer', 50000)
emp_2= Employee('Test', 'Employee', 60000)


# Regular method call
emp_1.fullname()
print('\nCreated class, regular methods and its instances')
print('------------------------------------------------')
print('\nEmployee 1: ')
print('Fullname:', Employee.fullname(emp_1))
print('Pay: ', emp_1.pay)
print('Email: ', emp_1.email)


# Static method call
import datetime
my_date= datetime.date(2021, 3, 7)
print('\nUsed static method to find isWorkingday?')
print('---------------------------------------')
print(my_date, ' Sunday' ,'\n Is working day? ', Employee.is_workday(my_date))
my_date= datetime.date(2021, 3, 7)
print(my_date,' Monday', '\n Is working day? ', Employee.is_workday(my_date))


# Class method call
print('\nUsed class method to set Raise amount')
print('-------------------------------------')
print(Employee.raise_amt)
print('Called set_raise_a class method')
Employee.set_raise_amt(1.05)
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)





