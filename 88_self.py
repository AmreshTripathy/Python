class Employee:
    company = 'Google'
    def getSalary(self):
        print (f'Salary for {self.name} working in {self.company} is {self.salary}')

amresh = Employee()
amresh.name = 'Amresh'
amresh.salary = 10000
amresh.getSalary()
# Employee.getSalary(amresh)
# actually amresh.getSalary() converts to Employee.getSalary(amresh) in machine point of view
