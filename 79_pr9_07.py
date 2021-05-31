text = True
i = 0

with open('log.txt') as f:
    while text:
        i += 1
        text = f.readline().lower()
        if ('python' in text):
            print (f'Yes, Python is present in line number {i}')
            
