# create a class Employee and add salary and increment properties to it

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self._salary=salary
        
    def __str__(self):
        return  (f'Name: {self.name}\n'
                f'Salary: {self._salary:,.2f}')
        
        
    def increment(self,percent):
        self._salary+=(self._salary * (percent/100))
    
     # getter
    @property
    def salary(self):
        return self._salary
    
    # setter
    @salary.setter
    def salary(self, value):
        if (value < 0):
            raise ValueError("Salary cannot be negative")
        self._salary = value
        
        

        
e1=Employee('Abdul Rehman',100000)
print(e1)
e1.increment(12)
print(e1)
e1.salary=10
print(e1)
        