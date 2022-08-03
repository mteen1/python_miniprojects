# Type your code here
def row_maximums(ndlist):
    
    output={}
    
    for i in range(len(ndlist)):
        max=0
        for num in ndlist[i]:
            if num>max:
                max = num
                
        output['row '+str(i)+' max'] = max
        
    return output

print(row_maximums([[5, 0, 0, 0, 13],
 [0, 12, 0, 0],
 [20, 0, 11, 0],
  [6, 0, 0, 8]]))
