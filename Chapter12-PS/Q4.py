# write a program to display a/b where a and b are integers.If b=0 display infinite by
# handling the ZeroDivisionError

a:int=int(input('Enter a:'))
b:int=int(input('Enter b:'))

res=None

try:
    res=a/b
except ZeroDivisionError as e:
    print('Infinte')
else:
    print(res)