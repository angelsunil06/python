'''
author:angel
date:3-12-24

'''
def gcd(n1,n2):
    if n1%n2==0:
        return n2
    else:
        return gcd(n2,n1%n2)
a=gcd(516,188)
print(a)