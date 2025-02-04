# FUNCTION ARGUMENTS AND RETURN STATEMENT

def average(a,b): # we can also give the values in this code of line .. eg - def average(a=9, b=0)
    print("The avg is", (a+b/2))
average(5,7) # when the values are given in the above code of line , the we can write "average()" only.

# lets print the name
def name(fname, mname="Gaurav", lname= "Sharma"):
    print("Hello,",fname, mname, lname)
name("Poorvi")