def four_letter(s):
    words=s.split()
    count=0
    for word in words:
        length=len(word)
        if length > 4:
           count+=1
    return count
words=input("give me words i will tell you how many of them have 4+ letters:\n")
print(four_letter(words))
