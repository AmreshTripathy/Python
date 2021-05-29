def sum(n):
    if (n == 0):
        return 0
    #return (n + sum(n-1))
    return ((n * (n+1)) / 2)

n = int(input('Enter the Value: '))
print (f'Sum of {n} is {sum(n)}')