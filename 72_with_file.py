# Benifits of with statement
# No need to use f.close to close the file. With statement automatically close the file
with open ('71_another.txt', 'r') as f:
    a = f.read()
print (a)
