# write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

words={
    'Book':'Kitab',
    'Pen':'Kalam',
    'Door':'Darwaza',
    'Window':'Khirki',
    'Chair':'Kursi'
}

search=input('Search Word with meaning:')

meaning=words.get(search)
print(f'{search}={meaning}')
