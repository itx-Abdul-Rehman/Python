# write a program to store seven fruits in a list entered by the user

fruits=[]
print('------------------------Enter seven fruits names-------------------------')
for i in range(7):
    name=input(f'Enter fruit {i+1} name:')
    fruits.append(name)
    
for i in range(len(fruits)):
    print(fruits[i])
    