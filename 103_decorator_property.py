class Employee:
    company = 'Bharat Gas'
    salary = 5600
    salaryBonus = 400
    # totalSalary = 6100
    
    @classmethod
    def printSalary(cls, val):
        cls.salary = val

    @property
    def totalSalary(self):
        return self.salary + self.salaryBonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salaryBonus = val - self.salary


e = Employee()
print (e.totalSalary)
e.printSalary(5500)
e.totalSalary = 5800

print (e.salary)
print (e.salaryBonus)
print (e.totalSalary)