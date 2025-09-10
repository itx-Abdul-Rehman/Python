# write a program using functions to find greatest of three numbers

def findGreatestNumber(num1,num2,num3):
    if(num1>num2 and num1>num3):
        return num1
    elif(num2>num1 and num2>num3):
        return num2
    else:
        return num3

numbers=[]

for i in range(3):
    number=int(input(f'Enter number {i+1}:'))
    numbers.append(number)
    
greatestNumber=findGreatestNumber(numbers[0],numbers[1],numbers[2])
print(f'Greatest Number is {greatestNumber}')