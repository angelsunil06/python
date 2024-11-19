mylist=[10,20,20,12,13,10]
uniquelist=[]
for number in mylist:
    if number not in uniquelist:
        uniquelist.append(number)
print('the original list is:',mylist)
print(uniquelist)
