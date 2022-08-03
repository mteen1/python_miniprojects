# Type your code here
def count_consonants(string):
    string=string.lower()
    count=0
    for i in string:
        if i!= "a" and i!="e" and i!="i" and i!="o" and i!="u" and i!=" ":
            count+=1


    return count


string=input("enter a string to count the consonants:\n")
print(count_consonants(string))
