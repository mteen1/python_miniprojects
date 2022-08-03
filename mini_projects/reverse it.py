def reverse_it(s):
    string=''
    character=''
    for char in s:
        if char.islower():
            character=char.upper()
            string=character+string
        elif char.isupper():
            character=char.lower()
            string=character+string
        else: string=char+string
        
    print(string)
user=input('enter a string to reverse it:\n')
reverse_it(user)
