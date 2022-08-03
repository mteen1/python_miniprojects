# Type your code here
def construct_dictionary_from_lists(names, ages, scores):
    output={}
    for i in range(len(names)):
        list=[]
        list.append(ages[i])
        list.append(scores[i])
        if scores[i] >= 60:
            list.append("pass")
        else: list.append("fail")
        output[names[i]] = list
        
    return output
