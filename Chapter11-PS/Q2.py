# create a class 'Pets' from a class 'Animals' and further create a class 'Dog' from 'Pets'.
# Add a method 'bark' to class 'Dog'

class Animal:
    def __init__(self):
        print('This is a Animal')
        

class Pet(Animal):
    def __init__(self):
        super().__init__()
        print('This is a Pet')
        
class Dog(Pet):
    def __init__(self):
        super().__init__()
        print('This is a Dog')
        
    
    def bark(self):
        print('Barking')
        
dog=Dog()
dog.bark()