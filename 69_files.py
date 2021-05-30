# use open function to read the content of a file
#f = open('69_sample.txt', 'r')
f = open('sample.txt')# By deafult is r
#data = f.read()
data = f.read(7) #read first 7 characters 
print (data)
f.close()
