# write a program to find whether a given number is prime or not

num=int(input('Enter a number:'))

isPrime=True
for i in range(2,num):
      if(num%i==0):
         isPrime=False
         break
        
if(isPrime and num>1):
    print(f'{num} is a prime number')
else:
    print(f'{num} is not a prime number')