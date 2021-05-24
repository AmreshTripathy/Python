a = set()
print (type(a))

# adding values to an empty set
a.add(4)
a.add(5)
# a.add([4, 5, 6]) You can not add list in a set
a.add((1, 2, 3)) # but you can add tuple in a set
# a.add({'amresh':'You are a hero'}) # dictionary can not be inserted in a set
print (a)

# Length of the set
print (len(a))# show thw length of the set

#Remove function of set
a.remove(5)# removes 5 from the set
print (a)

print (a.pop())# Removes an arbitary item from the set

print (a.clear())# Clear the set completely