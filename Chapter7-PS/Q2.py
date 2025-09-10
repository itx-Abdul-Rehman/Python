# Write a program to greet all the person names stored in a list 'l' and which starts with 'S'

l=["Harray","Soham","Sachin","Rahul"]


for i in range(len(l)):
    if(l[i].startswith('S')):
        print(f'Hello, {l[i]}')
        