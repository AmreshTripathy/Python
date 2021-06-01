from datetime import datetime

class Employee:
    company = 'Google'

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print ('Employee is created!')
        
    def getDetails(self):
        print (f'The name of the employee is {self.name}')
        print (f'The salary of the employee is {self.salary}')
        print (f'The subunit of the employee is {self.subunit}')

    def getSalary(self, signature):
        print (f'Salary of {self.name} working in {self.company} is {self.salary}\n{signature}' )

    @staticmethod
    def greet():
        print ('Good Morning, Sir!')

    @staticmethod
    def time():
        now = datetime.now()
        curr_time = now.strftime('%H:%M:%S')
        print (curr_time)

amresh = Employee('amresh', 1000, 'youtube')
# amresh = employee() throws an error 3 required positional argument
amresh.getDetails()

amresh.name = 'Harry'
amresh.salary = 10000

amresh.getSalary('Thanks!')
amresh.greet()
amresh.time()
