class Employee:
    company = 'Google'

    def getDetails(self):
        print ('Hi, Everyone')
    
class Programmer(Employee):
    language = 'Python'
    company = 'Youtube'
    def getLanguage(self):
        print (f'The language is {self.language}')
    
    def getDetails(self):
        print ('He is a prrogrammer.')

ep = Employee()
pg = Programmer()
pg.getDetails()
print (f'Company: {pg.company}')
pg.getLanguage()
