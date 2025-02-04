#EXCEPTIONAL HANDLING

a = input("Enter the number:")
print(f"multiplication of table of {a} is:")

try:
    for i in range(1,11):
     print(f"{int (a)} x {i} = {int (a)* i}")
except:
  print("invalid input")
print("issue occured")
print("bye bye")

print(".....2nd example")
try:
  num= int(input("Enter a int:"))
  a=[2,4]
  print(a[num])
except ValueError:
  print("num entered is not an int")
except IndexError:
  print("index error")  
