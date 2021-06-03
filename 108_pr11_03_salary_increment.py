class Employee:
    salary = 1000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return f'Salary afetr increment is {self.salary * self.increment}'

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sli):
        self.increment = sli / self.salary

e = Employee()
print(e.salaryAfterIncrement)
print (e.increment)
e.salaryAfterIncrement = 2000
print(e.salaryAfterIncrement)
print (e.increment)
