# write a program to find the factorial of a given number using for loop

n=int(input('Enter a number to find factorial:'))

fac=1
for i in range(1,n+1):
    fac=fac*i
    
print('Factorial is:',fac)