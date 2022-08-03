#this app check how many words start with a character
print("give me words and letters i will tell you how many word start with that")
def startwith(s,c):
    words=(s.split())
    count=0
    for word in words:
        word.lower
        if word[0]== c:
           count+=1
    return count
string=input("enter words seperated with ' '\n")
letter=input("enter the letter to check:\n")
print(startwith(string,letter))
