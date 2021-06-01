from datetime import datetime

class Employee:
    company = 'Google'

    def getSalary(self, signature):
        print (f'Salary for {self.name} working in {self.company} is {self.salary}\n{signature}' )

    @staticmethod
    def greet():
        print ('Good Morning, Sir!')

    @staticmethod
    def time():
        now = datetime.now()
        curr_time = now.strftime('%H:%M:%S')
        print (curr_time)

amresh = Employee()
amresh.name = 'Amresh'
amresh.salary = 10000
amresh.getSalary('Thanks!')
amresh.greet()
amresh.time()
