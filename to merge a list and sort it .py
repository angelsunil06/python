list1=[]
list2=[]
number=int(input('enter no of elements in the first list:'))
print('enter the elements of list1:')
for i in range(number):
          list1.append(int(input()))
number=int(input('enter no of elements in the second list:'))
for i in range (number):
    list2.append(int(input()))
print(list1,list2)
combined_list=list1+list2
print(combined_list)
even_list=[]
odd_list=[]
for i in combined_list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
even_list.sort()
odd_list.sort()
print(even_list)
print(odd_list)
merged_list=even_list+odd_list
print(merged_list)



