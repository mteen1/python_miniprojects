def my_final_grade_calculation(filename):

    file = open(filename, mode="r")
    data = file.readlines()
    mylist = []
    names=[]
    output = {}
    score = 0
    for line in data:
        names = line.strip().split(",")
        for i in range(1,len(names)):
            names [i] = int(names[i])
        mylist.append(names)
    for name in mylist:
        q = name[1:7]
        q.sort()
        q = q[2:]
        q_aver = sum(q)/4
        
        a = name[7:11]
        a.sort()
        a = a[1:]
        a_aver = (sum(a)/3)
        score = (q_aver/4) + (a_aver/4) + (name[11]/4) + (name[12]/4)
        name[0] = name[0].lower()
        if score >= 60:
            output[name[0]] = "pass"
        else:
            output[name[0]] = "fail"


        return output

        
