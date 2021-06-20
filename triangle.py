ang1=int(input())
ang2=int(input())
ang3=int(input())
#valid or invalid tringle
if (ang1!=0 and ang2!=0 and ang3!=0 and (ang1+ang2+ang3)==180):
    print("valid")
    flag=1
else:
    print("invalid")
    flag=0
if flag==1:
    if (ang1==ang2 and ang1==ang3):
        print("Equilateral Triangle")
    elif (ang1==ang2 or ang1==ang3 or ang2==ang3):
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
