# write a program to find the greatest of four numbers entered by the user

numbers=[]

for i in range(4):
    number=input(f'Enter numbe {i+1}:')
    numbers.append(number)

if(numbers[0]>numbers[1] and numbers[0]>numbers[2] and numbers[0]>numbers[3]):
    print(f'{numbers[0]} is greater than {numbers[1]},{numbers[2]},{numbers[3]}')
    
elif(numbers[1]>numbers[0] and numbers[1]>numbers[2] and numbers[1]>numbers[3]):
    print(f'{numbers[1]} is greater than {numbers[0]},{numbers[2]},{numbers[3]}')
    
elif(numbers[2]>numbers[0] and numbers[2]>numbers[1] and numbers[2]>numbers[3]):
    print(f'{numbers[2]} is greater than {numbers[0]},{numbers[1]},{numbers[3]}')
else:
     print(f'{numbers[3]} is greater than {numbers[0]},{numbers[1]},{numbers[2]}')