# Type your code here
def calculate_expenses(filename):
    file_pointer = open(filename, mode="r")
    data = file_pointer.readlines()
    output = []
    # print(data)
    for i in data:
        # mytuple = None
        z = i.replace(" ", "").split(",")
        z[1] = float(z[1])

        mytuple = (z[0], ("${:.2f}".format(z[1])))
        # print(mytuple)
        output.append(mytuple)
    output.sort()
    return output


print(calculate_expenses("expenses.txt"))
