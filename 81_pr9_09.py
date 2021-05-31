with open('copy.txt') as f:
    print (f.read())

with open('copy.txt', 'w') as f:
    f.write('')

with open('copy.txt') as f:
    print (f.read())