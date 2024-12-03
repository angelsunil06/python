'''
author:angel
date:3-12-24

'''
def addnumbers(n1,n2):
    if n2==0:
        return n1
    else:
        return addnumbers(n1+1,n2-1)
sum=addnumbers(5,3)
print(sum)