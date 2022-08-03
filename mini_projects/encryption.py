
def my_encryption(string):
    char_set =   "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    secret_key = "DdCAAbz2RHNPWhNOdEBvtVlpTa "
    outputstr=""
    count=0
    
    for char in string:
        count=0
        while char!=char_set[count]:
            count+=1
        outputstr=outputstr+secret_key[count]
    return outputstr


string=input("enter the secret messages:\n")
print(my_encryption(string))