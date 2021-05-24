myDict = {
    'Pankha': 'fan',
    'dabba': 'box',
    'vastu': 'items'
}
print ('Options are:',list(myDict.keys()))
a = input('Enter the HIndi word\n')
print ('The meaning of your word is:\n'+ str(myDict.get(a))) 
