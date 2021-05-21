letter = '''Dear <|Name|>,
You are selected!
Date: <|Date|>'''
name = input("Enter the name\n")
Date = input("Enter the date\n")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", Date)
print (letter)