def mostrepeated(s):
    string=s.lower()
    most=0
    count=0
    character=''
    for char in string:
        if char!=" ":
            count=string.count(char)
            if count>=most:
                most = count
                character=char
    print('the most repeated character is:',character)
    print('with', most, 'repeats')
string=input('enter a string:\n')
mostrepeated(string)
               
