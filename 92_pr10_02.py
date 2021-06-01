class calculator:
    def __init__(self, num):
        self.number = num
    
    def square(self):
        print (f'The value of {self.number} square is {self.number ** 2}.')
    
    def cube(self):
        print (f'The value of {self.number} cube is {self.number ** 3}.')
    
    def squareRoot(self):
        print (f'The value of {self.number} sqare-root is {self.number ** 0.5}.')

num = int(input('Enter a Number: '))
a = calculator(num)
a.square()
a.cube()
a.squareRoot()
