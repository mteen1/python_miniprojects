def anagrams(s1,s2):
    s1,s2=s1.lower(),s2.lower()
    a=0
    #if the length is different cant be anagram
    if len(s1)!= len(s2):
        return False
    for i in s1:
        for char in s2:

            if char == i:
                #replace makes sure no chars is counted twice
                #and break is to make sure after we found the matches dont continue
                a+=1
                s2=s2.replace(char,"",1)
                break

    if a == len(s1):
        return True
    else:
        return False


print('Are these words anagram?')
s1=input("s1:")
s2=input("s2:")
if anagrams(s1,s2):
    print("hell yes!")
else:
    print("nope!")
