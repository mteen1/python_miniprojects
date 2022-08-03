from grades_dict import *
def print_grades(file_name):
    # Call your create_grades_dict() function to create the dictionary
    grades = create_grades_dict(file_name)
    print("    ID     |       Name       | Test_1 | Test_2 | Test_3 | Test_4 |  Avg.  |")
    grades.sor
    for i in grades:
        output = ""
        ID = int(i)
        name = grades[i][0]
        one = grades[i][1]
        two = grades[i][2]
        three = grades[i][3]
        four = grades[i][4]
        average = grades[i][5]
        output = "{: <10d} | {:16s} | {:6d} | {:6d} | {:6d} | {:6d} | {:6.2f} |".format(ID ,name,one,two,three,four,average)
        print(output)

print_grades("student_grades.txt")
