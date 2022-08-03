def number_to_words(int):#4digit integers
    numbers={"1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine", "10":"ten", "11":"eleven", "12":"twelve", "13":"thirteen", "14":"fourteen", "15":"fifteen",
    "16":"sixteen", "17":"seventeen", "18":"eighteen", "19":"nineteen", "20":"twenty", "30":"thirty", "40":"forty", "50":"fifty", "60":"sixty", "70":"seventy", "80":"eighty",
     "90":"ninety", "0":""}
    string=str(int)
    output=""
    if string[0]!="0":
        output=numbers[string[0]]+" thousand and"
    if string[1] != "0":
        output += " " + numbers[string[1]] +" hundred and"

    if string[2]!="0" and string[3]=="0":
        output += " " + numbers[string[2:4]]

    if string[2] == "1" and string[3]!="0":
        output +=" "  + numbers[string[2:4]]

    if string[2] !="0" and string[2]!="1" and  string[3]!= "0":
        output +=" " + numbers[string[2]+"0"] +" " + numbers[string[3]]
    if string[2]=="0":
        output +=" " + numbers[string[3]]

    output=output.strip()
    return output


integer=input("enter a 4 digit to turn into words!\n")
print((number_to_words(integer)))
