# Create a class (2-D vector) and use it to create another class representing a 3-D vector

class TwoDVector:

    def __init__(self):
        print('This is a 2-D Vector and Calling from child class')
    

class ThreeDVector(TwoDVector):
    
    def __init__(self):
        super().__init__()
        print('This is a  3-D Vector')


threeD=ThreeDVector()
