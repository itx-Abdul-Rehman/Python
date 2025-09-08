# write a program to fill in a letter template given bellow with name and date
#'''Dear <|Name|>,
#Your are selected!
#<|Date|>'''

letter='''Dear <|Name|>,
Your are selected!
<|Date|>'''

replaceNameLetter=letter.replace('<|Name|>','Abdul Rehman')
replaceDateLetter=replaceNameLetter.replace('<|Date|>','09/08/2025');
print(replaceDateLetter)