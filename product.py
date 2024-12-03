'''
author:angel
date:3-12-24

'''
def productnumbers(n1,n2):
    if n2==1:
        return n1
    else:
       return n1+ productnumbers(n1,n2-1)
product=productnumbers(5,4)
print(product)