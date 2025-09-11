# create a class 'programmer' for storing information of few programmers working at Microsoft
import random

class Programmer:
    company='Microsoft'
    
    def __init__(self,name,phoneno,email,salary):
        self.id=random.randint(1000,9999)
        self.name=name
        self.phoneno=phoneno
        self.email=email
        self.salary=salary
        
    def getId(self):
        return self.id
    def getName(self):
        return self.name
    def getPhoneNo(self):
        return self.phoneno
    def getEmail(self):
        return self.email
    def getSalary(self):
        return self.salary
    def getCompany(self):
        return self.company
    
    def setName(self,name):
        self.name=name
    def setPhoneNo(self,phoneno):
        self.phoneno=phoneno
    def setEmail(self,email):
        self.email=email
    def setSalary(self,salary):
        self.salary=salary
    
    def getInfo(self):
        print(f'Id:{self.id}')
        print(f'Name:{self.name}')
        print(f'Email:{self.email}')
        print(f'Phone No:{self.phoneno}')
        print(f'Salary:{self.salary}')
        print(f'Company:{self.company}')
    
    
    
employee1=Programmer('Abdul Rehman','0301 6852342','abdul@gmail.com',100000)
employee1.getInfo()

employee2=Programmer('Ali','0301 6231342','ali@gmail.com',100000)
employee2.getInfo()

employee3=Programmer('Haris','0301 6567342','haris@gmail.com',100000)
employee3.getInfo()

employee4=Programmer('Dawood','0301 6858762','dawwod@gmail.com',100000)
employee4.getInfo()