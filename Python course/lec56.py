# OOPS concept in python

def hello():
    print("hello")
hello()    

class person:
    name = "Poorvi"
    occupation = "engineer"
    salary = 90000
    def info(self):
        print(f"{self.name} is a {self.occupation} ")
a = person()   
a.name = "Vani"
a.occupation = "HR"    
a.info() 