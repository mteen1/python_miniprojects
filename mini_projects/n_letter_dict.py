def n_letter_dictionary(my_string):
    string = my_string.lower().split()
    output = {}
    
    string = list(dict.fromkeys(string))
    
    string.sort(key=len, reverse=True)
    
    length = len(string[0])
    for i in range(length,0,-1):
        mylist = []
        for item in string:
            if len(item)==i:
                mylist.append(item)

        if mylist!=[]:
            mylist.sort()
            output[i] = mylist
        
        
    return output

print(n_letter_dictionary("The way you see people is the way you treat them and the Way you treat them is what they become"))
