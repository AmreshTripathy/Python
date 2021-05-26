m = []
for i in range(3):
    sub = int(input('enter mark of subject '+str(i+1)+': '))
    if (sub <= 100):
        m.append(sub)
    else:
        print ('Mark should not be greater than 100')
        break

if (m[0]<33 or m[1]<33 or m[2]<33):
    print ('You are fail')
elif (((sum(m)/300)*100)<40):
    print ('You fail due to total percentage less than 40%')
else:
    print ('''Congatulation! You are PASS
    Total Mark: '''+ str(sum(m)))