def listeven(list):
    list=list.split()
    big=0
    for i in list:
        for num in i:
            if num%2==False:
                big=num
            else:
                return None
            
    return big

mylist=input("enter a 2d list:\n")
listeven(mylist)