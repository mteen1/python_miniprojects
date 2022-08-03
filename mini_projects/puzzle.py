CZA = 'RTRDSHGMRDP'
CDN = 'ZTTFFSSEN'
TR= 'DKPCFGS'
FOTR = 'FSGLGABM'
DS = 'LGGSWP'
RN = 'IVXLCD'
SR = 'DDPVCCBR'
AS = 'ATGCLVLSCAP'
mylist = [CZA,CDN,TR,FOTR,DS,RN,SR,AS]
for i in range(8):
    mylist[i] = sorted(set((mylist[i])))
    print(mylist[i])