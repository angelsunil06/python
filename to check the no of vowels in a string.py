'''
name:angel
date:29 october 2024
version:1.0
'''

string=input('enter a string:')
count=0
vowels='aeiouAEIOU'
for i in string:
    if i in vowels:
        count+=1
print('no of vowels in the given string:',count)
