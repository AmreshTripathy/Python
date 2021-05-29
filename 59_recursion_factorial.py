# n = int(input('Enter a number: '))
# product = 1
# for i in range(1, n+1):
#     product = product * i
# print (product)

# def factorial_iter(n):
#     product = 1
#     for i in range(1, n+1):
#         product = product * i
#     return product

def factorial_recurse(n):
    if ( n == 1 or n == 0):
        return 1
    return n * factorial_recurse(n-1)

n = int(input('Enter a Number: '))
print (factorial_recurse(n))