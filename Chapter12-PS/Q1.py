# ------------------------------Advanced Python I------------------------------- 
#  walrus :=  if(n:=len(list)<10)
#  num:int=7     //type
#  def(a:int,b:int)->int: return 10   //type
#  try except (else,finally),raise 
#  match - case
#  enumerate
#  list comprehension
#  __name__ , __main__ , print(__name__) if same file run than '__main__' otherwise where import 'filename'
#  global keyword
#  with (open() as f1
#       open() as f2):

try:
  with (
    open('1.txt','r') as f1,
    open('2.txt','r') as f2,
    open('3.txt','r') as f3,):
    pass
    
except Exception as e:
    print('File not exist')
