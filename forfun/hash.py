import hashlib
from itertools import permutations

strs='my name is matin and my id number is 1362969850'
lis2=list(strs)+list(strs.upper())

for x in permutations(lis2, len(strs)):
    print(x)
    if ''.join(x) != strs:
        s = ''.join(x)
        print(s)
        hash = hashlib.sha256()
        hash.update(s.encode('UTF-8'))
        hash = hash.hexdigest()
        if hash[-4:] == '1111':
            print('found it! the string is', s)
            break
        else:
            print(hash)