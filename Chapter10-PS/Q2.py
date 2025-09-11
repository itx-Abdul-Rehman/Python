# write a class 'calculater' capable of finding square, cube and square root of a number

import math

class Calculator:
    def __init__(self,x):            
        self.x=x
        
    def square(self):
        return self.x**2
    
    def cube(self):
        return self.x**3
    
    def squareRoot(self):    
        return (round((self.x**0.5),2))
    
    @staticmethod
    def greet():
        print('Hello')

cal=Calculator(8)
print(f'Square: {cal.square()}')
print(f'Cube: {cal.cube()}')
print(f'Sqaure Root: {cal.squareRoot()}')
cal.greet()