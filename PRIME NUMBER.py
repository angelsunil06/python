number=int(input('enter a number:'))
isprime=True
for i in range(2,number//2+1):
    if number % i==0:
        isprime=False
        break
if isprime:
    print('the given number',number,'is a prime number')
else:
    print('the given number',number, 'is not a prime number')


