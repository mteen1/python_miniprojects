def find_word_horizantal(crossword,word):
    #we bulid a list  of possible words
    mylists=[]
    for list in crossword:
        characters=""
        for char in list:
            characters += char
            
        mylist.append(characters)

    # now we check the word with each possible word in list
    row = ""
    for i in range(len(mylist)):
        if word in mylist[i]:
            row = i
            break
    
    #now we find the column
    len_word = len(word)
    len_char = len(mylist[row])
    for i in range(len_char):
        if mylist[row][i:i+len_word] == word:
            column = i
            break
        
    output=[]
    output.append(row)
    output.append(column)
    return output
