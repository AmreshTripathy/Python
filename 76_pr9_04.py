with open('sample.txt') as f:
    content = f.read()
    print (content,'\n')

content = content.replace('donkey', '######')

with open('sample.txt', 'w') as f:
    f.write(content)

with open('sample.txt') as f:
    print (f.read())
