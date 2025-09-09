# write a program to find out whether a student has passed or failed if it requires a total of 
# 40% and at least 33% in each subject to pass. Assume 3 subjects and take  marks as a input from the user.

studentsResult={};

totalMarks=300;
obtainedMarks=0;
eachSubjectPass=True
for i in range(3):
    subject=input(f'Enter subject name {i+1}:')
    mark=int(input(f'Enter marks subject {i+1} out of 100:'))
    studentsResult.update({subject:mark})
    obtainedMarks=obtainedMarks+mark
    if(mark<33):
        eachSubjectPass=False
    
    
percentage=(obtainedMarks/totalMarks) * 100

if(percentage>=40 and eachSubjectPass):
    print('Student passed!')
else:
    print('Student failed!')