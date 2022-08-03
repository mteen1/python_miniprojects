from find_mismatch import *
from siod import single_insert_or_delete as siod


def corrector(wrong, correct):
    # s1 is the wrong string
    # s2 is the correct list of words

    # first we define 2 functions
    # this function finds a mismatch between
    # 2 strings with same length
    #
    # main_function
    wrongstr = wrong.lower().split()
    print(wrongstr)
    for i in correct:
        i.lower()

    output = ""
    mylist = []

    for word in correct:
        for i in wrongstr:
            if find_mismatch(i, word) is not False:
                mylist.append(find_mismatch(i, word))
            if siod(i, word) is not False:
                mylist.append(siod(i, word))
            print(mylist)
    for i in range(len(wrongstr)):
        if len(wrongstr[i]) <= 2:
            mylist[i] = wrongstr[i]


clist = (input("enter the correct order of words"))
wrong = input("enter the wrong string")
corrector(wrong, clist)
