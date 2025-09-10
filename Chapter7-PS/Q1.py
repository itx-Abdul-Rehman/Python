# write a program to print multiplication table of a given number using for loop

number=int(input('Enter a number to print multiplication table:'))

for i in range(10):
    print(f'{number} * {i+1}=',(number*(i+1)))
else:
    print('Done')