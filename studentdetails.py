'''
author:angel
date:1 october 2024
version:1.0
'''
name=input('enter the student name:')
rollno=int(input('enter roll no:'))
rollno=rollno+1
cgpa=float(input('enter cgpa'))
percentage_marks=cgpa*10
print('name of the student is:',name)
print('rollno of the student:',rollno)
print('marks in percentage:',percentage_marks,end='%')
