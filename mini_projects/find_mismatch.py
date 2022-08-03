#this app finds the mismatch between strings
def find_mismatch(s1,s2):
    s1=s1.lower()
    s2=s2.lower()
    count=0
    if s1 == s2:
        return 0
    
    for x in range(0, len(s1)):
        if len(s1)==len(s2):
            if s1[x]==s2[x]:
                count+=1
            if count==len(s1) or count==(len(s1)-1):
                return 1

    else:
        return 2


s1=input("enter the first string:\n")
s2=input("enter the second string:\n")
print(find_mismatch(s1,s2))
