class Person:
    country = 'India'

    def takeBreath(self):
        print ('I am breathing...')

class Employee(Person):
    company = 'Honda'

    def getSalary(self):
        print (f'Salary is {self.salary}')

    def takeBreath(self):
        print ('I am an employee, So I am luckily breathing...')

class Programmer(Employee):
    company = 'Fiverr'

    def getsalary(self):
        print ('No Salary to Programmers')

    def takeBreath(self):
        print ('I am a programmer, so I am breathing...')
        
p = Person()
p.takeBreath()

e = Employee()
e.takeBreath()
print (e.company) 

pr = Programmer()
pr.takeBreath()
print (pr.company)
print (pr.country)
