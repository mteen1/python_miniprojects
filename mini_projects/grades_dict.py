def create_grades_dict(file_name):
    file = open(file_name,mode = 'r')
    lines = file.readlines()
    mylist = []
    output = {}
    average = 0
    for i in range(len(lines)):
        value = [0,0,0,0,0,0]
        
        lines[i] = lines[i].replace(" ","")
        mylist.append(lines[i].split(","))
        value[0]= mylist[i][1]
        if "Test_1" in mylist[i]:
            a = mylist[i].index("Test_1")
            value[1] = int(mylist[i][a+1])
        else : value[1] = 0
        if "Test_2" in mylist[i]:
            a = mylist[i].index("Test_2")
            value[2] = int(mylist[i][a+1])
        else : value[2] = 0
        if "Test_3" in mylist[i]:
            a = mylist[i].index("Test_3")
            value[3] = int(mylist[i][a+1])
        else : value[3] = 0
        if "Test_4" in mylist[i]:
            a = mylist[i].index("Test_4")
            value[4] = int(mylist[i][a+1])
        else: value[4] = 0
        average = (value[1] + value[2] + value[3] + value[4])/4
        value[5] = average
        output[mylist[i][0]] = value


    return output

print(create_grades_dict("student_grades.txt"))
