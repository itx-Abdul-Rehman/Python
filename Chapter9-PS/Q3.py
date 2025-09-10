# write a program to generate multiplication tables 2 to 20 and write it to the different files.
# Place these files in a folder for a 13 - year old
import os

def saveInFile(filename,line):
    with open(filename,'a') as f:
        f.write(line)

def genrateTables(n):
    if(n>20):
        return
    
    for i in range(1,11):
         line=str(n)+' * '+ str(i) +'='+str((n*i))+'\n'
         saveInFile('13-yearold/table-' + str(n) + '.txt',line)
    
    return genrateTables(n+1)

os.makedirs('13-yearold', exist_ok=True)
genrateTables(2)