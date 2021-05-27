post = 'Hi hello this is amresh how can ihelp you please help others to do their work'
x = input('Enter the word to find it exist or not\n')
if (x in post):
    print ('Exist')
elif (x.upper() in post):
    print ('Exist')
elif (x.lower() in post):
    print ('Exist')
elif (x.capitalize() in post):
    print ('Exist')
else:
    print ('Not Exist')