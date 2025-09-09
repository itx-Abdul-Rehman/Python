#  write a programs to which finds out whether a given name is present in a list or not

list=[32,34,54,67,89,3,2]

number=int(input('Enter a number:'))

if(list.count(number)>0):
    print(f'{number} is present in the list')
else:
    print(f'{number} is not present in the list')