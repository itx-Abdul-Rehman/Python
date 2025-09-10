# write a recursive function to calculate the sum of first n natural numbers

def sum(number,s):
    if(number==0):
        return s

    s=s+number
    return sum(number-1,s)

number=int(input('Enter number (n):'))

s=sum(number,0)
print(f'Sum is: {s}')