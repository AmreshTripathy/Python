import re
x = int(input())
for _ in range(x):
    s = input()
    try:
        re.compile(s)
        print ("True")
    except Exception as e:
        print ("False")