#python object-oriented programming
class Employee:

    raise_amt= 1.04

    def __init__(self, first, last, pay):
         self.first= first
         self.last= last
         self.email= first+'.' + last + '@email.com'
         self.pay= pay

    def fullname(self):
        return'{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay= int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt= 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang=prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self. employees=[]
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->',emp.fullname())

            
dev_1= Developer('Corey', 'Schafer', 50000,'Python')
dev_2= Developer('Test', 'Employee', 60000, 'Java')

##print('\nDeveloper class instance')
##print(dev_1.email)
##print(dev_1.prog_lang)
##print(dev_1.pay)
##print('\nApply raise')
##dev_1.apply_raise()
##print(dev_1.pay)

print('\nManager class instance')
mgr_1= Manager('Sue', 'smith', 90000, [dev_1])
      
print('\nIs mgr_1 Instance of Employee?')
print(isinstance(mgr_1, Employee))
      
print('\nIs Manager subclass of Employee?')
print(issubclass(Manager,Employee))

print('\n')
print(mgr_1.email)
mgr_1.add_emp(dev_2)
##mgr_1.remove_emp(dev_1)
mgr_1.print_emps()
