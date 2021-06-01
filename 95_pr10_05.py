import random
booked = []
class Train:
    company = 'Indian Railways'
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def yesNoBookTicket(self):
        x = input('Do you want to book a ticket?\nYes or No: ')
        if (x == 'Yes' or x == 'yes' or x == 'Y' or x == 'y'):
            ticket = int(input('How many number of ticket you want to purchase: '))
            print (f'Total price: {fare * 3}')
            for i in range(ticket):
                intercity.bookTicket()
            print (f'No.{booked} Booked for you')
            print ('---------------------------------------------------')
            intercity.getStatus()
        elif(x == 'No' or x == 'no' or x == 'N' or x == 'n'):
            pass
        else:
            print ('Sorry! I am Unable to understand.\nPlease Enter a valid Input')
            intercity.yesNoBookTicket()

    def bookTicket(self):
        if (self.seats > 0):
            rand = random.randint(1,self.seats)
            booked.append(rand)
            self.seats -= 1
        else:
            print ('Sorry! This train is full. Kindly try in Tatkal.\n')

    def getStatus(self):
        print (f'The name of the train is {self.name}')
        print (f'The seats available in the train is {self.seats}')

    def getFareInformation(self):
        print (f'The price  if the ticket for single person is {self.fare}/-\n')

    def yesNoCancelTicket(self):
        y = input('Do you want to cancel the ticket?\nYes or No: ')
        if (y == 'Yes' or y == 'yes' or y == 'Y' or y == 'y'):
            intercity.cancelTicket()
        elif (y == 'No' or y == 'no' or y == 'N' or y == 'n'):
            pass
        else:
            print ('Sorry! I am Unable to understand.\nPlease Enter a valid Input')
            intercity.yesNoCancelTicket()

    def cancelTicket(self):
        if (len(booked) != 0):
            k = int(input('Enter Your seat no. to cancel: '))
            if (k in booked):
                booked.remove(k)
                print (f'Ticket No.{k} is cancelled.')
                self.seats += 1
                print (f'Now you have No.{booked} tickets.')
            elif (k not in booked):
                print (f'You have entered a wrong no.\nNo.{k} is not booked yet.\nEnter again')
                intercity.cancelTicket()
        else:
            print ('You have not booked any ticket yet.\nSo, You can not cancel any ticket.')

name = input('Enter the name of the Train: ')
fare = float(input('Enter the price of a ticket: '))
seats = int(input('Enter No. of seats available: '))
intercity = Train(name, fare, seats)

print ('---------------------------------------------------')
intercity.getStatus()
intercity.getFareInformation()
print ('---------------------------------------------------')
intercity.yesNoBookTicket()
print ('---------------------------------------------------')
intercity.yesNoCancelTicket()
print ('---------------------------------------------------')
