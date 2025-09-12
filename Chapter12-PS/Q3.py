# write a list comprehension to print a list which contains the multiplication table of a user entered


n:int=int(input('Enter a number:'))

table=[i*n for i in range(1,11)]

with open('Tables.txt','a') as f:
    f.write(f'{table}\n')