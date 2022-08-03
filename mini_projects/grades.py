def calculate_grades(file_name):
    # Make a connection to the file
    file_pointer = open(file_name, 'r')
    
    data = file_pointer.readlines()
    output = []
    for i in data:
        student = i.replace(" ","").split(",")
        average = (int(student[1]) + int(student[2]) + int(student[3]) + int(student[4])) /4
        mytuple = (student[0] ,average)
        output.append(mytuple)


    output = tuple(sorted(output))

    return output
print(calculate_grades("student_grades.txt"))
