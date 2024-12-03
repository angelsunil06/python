'''
author:angel
date:3-12-2024
'''

def factorial(n):
       if n==0:
           return 1
       else:
           return n*factorial(n-1)
f=factorial(5)
print(f)