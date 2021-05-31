with open('log.txt') as f:
    text = f.read().lower()

if ('python' in text):
    print ('Yes, Python is present')
else:
    print ('No, Python is not present')
