# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key 
# as theri names. Asume that names are unique

myDictonary={}

for i in range(4):
    print(f'Friend {i+1}')
    key=input('Enter Key:')
    value=input('Enter Value:')
    myDictonary.update({key:value})
    
print(myDictonary)
