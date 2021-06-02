class Person:
    country = 'India'

    def __init__(self):
        print ('Intializing Person...\n')

    def takeBreath(self):
        print ('I am breathing...')

class Employee(Person):
    company = 'Honda'
    salary = 20000

    def __init__(self):
        super().__init__()
        print ('Intializing Employee...\n')

    def getSalary(self):
        print (f'Salary is {self.salary}')

    def takeBreath(self):
        super().takeBreath()
        print ('I am an employee, So I am luckily breathing...')

class Programmer(Employee):
    company = 'Fiverr'

    def __init__(self):
        super().__init__()
        print ('Intializing Programmer...\n')

    def takeBreath(self):
        super().takeBreath()
        print ('I am a programmer, so I am breathing...')
        
# p = Person()
# p.takeBreath()

#e = Employee()
# e.takeBreath()

pr = Programmer()
# pr.takeBreath()

