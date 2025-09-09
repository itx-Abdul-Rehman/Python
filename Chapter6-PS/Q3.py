# A spam comment is defined as a text containing following key words:
# Make a lot of maoney, buy now, subscribe this, click this
# write a program to detect these spams

spamComments=['make a lof of money','buy now', 'subscribe this', 'click this']

sentance=input('Enter a sentance:')


if(sentance.lower().count(spamComments[0])>0 or sentance.lower().count(spamComments[1])>0 
   or sentance.lower().count(spamComments[2])>0 or sentance.lower().count(spamComments[3])>0):
    print('Spam');
    
else:
    print('Not spam')