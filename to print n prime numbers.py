limit=int(input('enter limit:'))
for i in range(2,limit+1):
    isprime=True
    for num in range(2,(i//2)+1):
          if i % num ==0:
             isprime = False
             break
    if isprime:
         print(i)
    



