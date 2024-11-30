def righttrianglecheck():
    a=int(input('enter first side:'))
    b=int(input('enter second side:'))
    c=int(input('enter third side:'))
    list1=[a,b,c]
    list1.sort()
    if list1[2]**2==list1[0]**2+list1[1]**2:
        print('it is a right triangle')
    else:
        print('it is not a right triangle')
righttrianglecheck()