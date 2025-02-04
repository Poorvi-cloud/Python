#FINALLY KEYWORD IN PYTHON
def func1():
  try:
    a=[1,3,2,5]
    i= int(input("enter the index: "))
    print(a[i])
    return 2
  except:
    print("error occured")
    return 1
  finally:
    print("always executed")
x = func1()
print(x)
