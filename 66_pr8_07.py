def remove_and_split(string, word):
    newStr = string.replace(word, '')
    return newStr.strip()


string = '    Amresh is a Good boy    '
print (string)
word = input('Enter the word that you want to Replace: ')
n = remove_and_split(string, word)
print (n)

# print (this)
# print (this.strip())