# write a program to print third ,fifth and seventh element from a list using enumerate function

list=[1,2,3,4,5,6,7,8,9,10]

for index,element in enumerate(list):
    if(index==2 or index==4 or index==6):
        print(f'Element {index+1}: {list[index]}')
        