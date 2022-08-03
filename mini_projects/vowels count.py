def vletters(s):
    vowels=['A','a','E','e','O','o','U','u','I','i']
    count=0
    for char in s:
        if char in vowels:
           count+=1

    return count
string='how many vowels this hAas?'
print(vletters(string))
