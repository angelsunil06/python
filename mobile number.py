def mobilenumbercheck():
    number = input('enter the number:')
    if len(number)==10 and number[0]in'789':
         print('the mobile number is valid')
    else:
        print('the mobile number is not valid')
mobilenumbercheck()
