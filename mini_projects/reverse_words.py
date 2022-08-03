def reverse_words(s):
    string=s.split()
    for x in range(0, len(string)):
        string[x]=string[x][::-1]
    output=''
    for x in range(0,len(string)):
        output+=string[x]+' '

    output=output.strip()
    print(output)

mystring=input('enter a string to reverse the worlds:\n')
reverse_words(mystring)
