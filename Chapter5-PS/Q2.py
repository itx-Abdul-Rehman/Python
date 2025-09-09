# write a program to input eight numbers from the user and display all the unique number(once)

numbers=[]

for i in range(8):
    number=int(input(f'Enter number {i+1}:'))
    numbers.append(number)
    
numbersWithOnce=set();
for i in range(len(numbers)):
    numbersWithOnce.add(numbers[i])
    
print(numbersWithOnce)