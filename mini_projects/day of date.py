def day_of_date(string):
    mylist=string.lower().split()
    months={
    "march":1,
    "april":2,
    "may":3,
    "june":4,
    "july":5,
    "august":6,
    "september":7,
    "october":8,
    "november":9,
    "december":10,
    "january":11,
    "february":12}
    week={
    0:"Sunday",
    1:"Monday",
    2:"Tuesday",
    3:"Wednesday",
    4:"Thursday",
    5:"Friday",
    6:"Saturday"}
    m=months[mylist[0]]
    c=int(mylist[2][:2])
    
    d=int(mylist[1])
    if m==12 or m==11:
        y=int((mylist[2][2:4]))-1
    else: y=int(mylist[2][2:4])
    
    w=((d + (int(2.6*m - 0.2))- (2*c) + y
       + (int(y/4)) +(int(c/4))))%7
    print(w)
    output= week[w]
    print(output)
date=input("enter date:\n")
day_of_date(date)
