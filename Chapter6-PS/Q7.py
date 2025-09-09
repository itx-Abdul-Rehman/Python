# Write a program to find out given post is taking about "Abdul" or not

postDescription=input('Post Describe:')

if(postDescription.lower().count('abdul')>0):
    print('Post is talk about \'Abdul\'')
else:
    print('Post is not talk about \'Abdul\'')