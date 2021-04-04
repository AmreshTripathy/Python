a = int(input())
b = int(input())
if(1 <= a <10**10):
    if(1 <= b <= 10**10):
        print(a+b)
        print(a-b)
        print(a*b)
else:
    print("limit range exceeded")