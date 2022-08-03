def numfinder(dict,int):
    keys=list(dict.keys())
    output=[]
    for key in keys:
        mylist= dict[key]
        for i in mylist:
            if i==int and (key not in output):
                output.append(key)
                
                
    return output
a={'ali':[2,3,3,5],'matin':[2,4,5],'z':[3]}
print(numfinder(a,3))
