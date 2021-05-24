My_Dict = {
    'fast': 'In a quick Manner',
    'Amresh': 'Hello! Amresh',
    'marks': '[1,2,3]',
    'secondDict': {'amresh': 'Hero'},
    1:2
}

print (list(My_Dict.keys())) # print the keys of the dictionary
print (My_Dict.values()) # print the values of the dictionary
print (My_Dict.items()) # print all the key,values

updatedict = {
    'lovish': 'friend',
    'Divya': 'friend',
    'Amresh': 'A handsome boy' # update the the previously existed key in the dictionary
}
My_Dict.update(updatedict)
print (My_Dict)

print (My_Dict.get('marks')) # prints value associated with 'marks'
print (My_Dict['marks']) # prints value associated with 'marks'

# The difference between .get & [] syntax dictionaries
print (My_Dict.get('marks2')) # returns None as 'marks2' not present in the dictionary 
print (My_Dict['marks2']) # throws the error as 'marks2' does not present in the dictionary