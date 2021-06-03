class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num1):
        print ('Lets add')
        return self.num + num1.num

    def __Sub__(self, num1):
        print ('Lets Substract')
        return self.num - num1.num

    def __mul__(self, num1):
        print ('Lets multiply')
        return self.num * num1.num

    def __truediv__(self, num1):
        print ('Lets divide')
        return self.num / num1.num

    def __floordiv__(self, num1):
        print ('Lets do Floor Division')
        return self.num // num1.num

    def __str__(self):
        return f'Decimal Number: {self.num}'

    def __len__(self):
        return 1

n = Number(9)
print (n)

print (len(n))
