# Type your code here
def find_longest_word(string):
    string=string.strip().split()
    longest=""
    for i in string:
        if len(i)>= len(longest):
            longest=i
    return longest
  
string=input("enter couple of words i will give you the longest:\n")
print(find_longest_word(string))
