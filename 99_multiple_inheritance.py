class FreeLancer:
    company = 'Fiverr'
    level = 0

    def upgradeLevel(self):
        self.level += 1

class Employee:
    company = 'Visa'
    ecode = 120

class Programmer(FreeLancer, Employee):
    name = 'Rohit'

p = Programmer()
p.upgradeLevel()
print (p.company)
