# checks if a string is palindrome
def isthispld(s):
    # reverse the string
    def reverse_str(s):
        r = ''
        for char in s:
            r = char + r
        return r

    string = s.lower()
    r = reverse_str(string)
    if r == string:
        return True
    else:
        return False


string = input("type the word and I will tell you if its palindrome?\n")
print(isthispld(string))
