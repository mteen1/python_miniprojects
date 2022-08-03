def list_to_tuple(list2d):
    list =[]
    for i in list2d:
        inlist = []
        for j in range(len(i)):
            inlist.append(i[len(i)-1-j])
        list.append(tuple(inlist))

    output = tuple(list)
    return output



print(list_to_tuple([['mean', 'really', 'is', 'jean'],
 ['world', 'my', 'rocks', 'python']]))
