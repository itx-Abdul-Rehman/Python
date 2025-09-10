# write a program to find first n natural number sum using while loop


n=int(input('Enter number (n):'))

i=0
sum=0
while(i<n):
    sum=sum+i
    i+=1
    
print('Sum is:',sum)