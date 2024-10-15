'''
author: angel
date: 14 october 2024
version: 1.0
program to calculate the sum of digits of a number
'''
num=int(input('enter a number:'))
sum=0
while num>0:
    re=num%10
    sum=sum+re
    num=num//10
print(sum)