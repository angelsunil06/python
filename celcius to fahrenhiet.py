'''
author:angel
date:22 october 2024
version:1.0
'''
temperature=int(input('enter temperature:'))
scale=input('is this in (c)elsius or (f)ahrenhiet?:')
if scale=='C':
     f=9/5*temperature+32
     print(temperature,'celcius is',f, 'fahrenheit')
else:
    f=9/5*(temperature-32)
    print(temperature,'fahrenhiet is',f,'celcius')