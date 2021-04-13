# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
mydict = {}
for i in range(n):
    data = list(input().rstrip().split())
    mydict[data[0]] = data[1]
mydict_keys = mydict.keys()
while True:
    try:
        name = input()
        if name in mydict_keys:
            print(name+"="+mydict[name])
        else:
            print("Not found")
    except:
        break
    
