def multiplication(n):
    for i in range(1, 11):
        print (f'{n} * {i} = {n * i}')

n = int(input('Enter a number: '))
multiplication(n)