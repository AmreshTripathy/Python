class Employee:
    company = 'Google'

    def showDetails(self):
        print ('This is an employee')
    
class Programmer(Employee):
    language = 'Python'
    company = 'Youtube'
    def getLanguage(self):
        print (f'The language is {self.language}')
    
    def showDetails(self):
        print ('This is a prrogrammer.')

e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print (p.company)
p.getLanguage()
