# RAISING CUSTOM ERROR IN PYTHON

a= int(input("enter no. btweem 5 and 9: "))
if(a<5 or a>9):
    raise ValueError("value should be between 5 and 9")

print(".......2nd ex")
a = input("Enter any value between 5 and 9. Write 'quit' to quit:")
def myfuc():
  if a=="quit":
    print("program quitted")
  else:
    if(int(a)<5 or int(a)>9):
     raise ValueError("Value should be between 5 and 9")
    else:
      print(a)
myfuc()