words = ['donkey', 'kaddu', 'mote']

with open('sample.txt') as f:
    content = f.read()
    print (content,'\n')

for word in words:
    content = content.replace(word, '######')

with open('sample.txt', 'w') as f:
        f.write(content)

with open('sample.txt') as f:
    print (f.read())
