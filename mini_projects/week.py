from collections import defaultdict
week = defaultdict(lambda: 'what?? :(')
week['1']='MONDAY',
week['2']='TUESDAY'
week['3']='WEDNESDAY'
week['4']= 'THURSDAY'
week['5']='FRIDAY'
week['6']='SATURDAY'
week['7']='SUNDAY'
x=(input("what day you want?\n"))
print(week[x])