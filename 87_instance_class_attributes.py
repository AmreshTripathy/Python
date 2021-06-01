class Employee:
    company = 'Google'
    salary = 100

harry = Employee()
rajni = Employee()
# Creating instance attribute for both the class
harry.salary = 300
# rajni.salary = 400
print (harry.salary)
print (rajni.salary)
# Throws an error because there is no instances of address
# print (rajni.address)
