# CONSTRUCTORS IN PYTHON

class person:

    def __init__(self,n,o):
        print("hey")
        self.name = n
        self.occ = o
    def info(self):
        print(f"{self.name} is {self.occ}")

a = person("poorvi", "developer")
b = person("vani", "hr")            
a.info()
b.info( )     
