# write a class 'Complex' to represent complex numbers along with overloaded operaters '+' and '*'
# which adds and multiplies them

class Complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def __add__(self,other):
        self_a=int(self.a)
        other_a=int(other.a)
        self_b=int(self.b[0:len(self.b)-1])
        other_b=int(other.b[0:len(other.b)-1])
        
        ans=f'{(self_a+other_a)}+{(self_b+other_b)}i'
        return ans
    

c1=Complex('3','4i')
c2=Complex('1','2i')

print(c1+c2)