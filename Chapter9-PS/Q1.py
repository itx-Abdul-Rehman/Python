# write a program to read the text from a given file 'poem.txt' and find out whether it conatins the word
# 'twinkle'


contains=False
line=None
with open("poem.txt",'r') as f:
    while(line!=''):
        line=f.readline()
        if((line.lower().count('twinkle'))>0):
            contains=True
            break
        
if(contains):
    print('Yes, twinkle word conatin in the \'peom.txt\' file')
else:
    print('No, twinkle word conatin in the \'peom.txt\' file')
    
