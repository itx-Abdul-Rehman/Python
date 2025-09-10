# write a program to print multiplication table of a given number using while loop

number=int(input('Enter a number to print multiplication table:'))
i=0
while(i<10):
     print(f'{number} * {i+1}=',(number*(i+1)))
     i += 1
