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

n1 = Number(6)
n2 = Number(4)
# sum = n1 + n2
print (n1.__add__(n2))
# mul = n1 * n2
print (n1.__Sub__(n2))
print (n1.__mul__(n2))
print (n1.__truediv__(n2))
print (n1.__floordiv__(n2))