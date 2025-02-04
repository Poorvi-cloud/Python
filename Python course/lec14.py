
# Conditional operators
# >, <, >=, <=, ==, !=


# IS ELSE STATEMENT
a=int(input("enter your age:"))
print("your age is",a)
print(a>18)
print(a==18)
print(a<=18)
print(a!=18)
if (a>18):
    print("You can drive.")
else:
    print("you cannot drive.")

# ELIF STATEMENT

num = int(input("Enter the value of num:"))
print(num)
if(num<0):
    print("num is negative")
elif(num==0):
    print("the num is zero")
else:
    print("the num is positive")

# NESTED IF STATEMENT

num = 18
if(num<0):
    print("the num is negative.")
elif(num>0):
    if(num>=10):
        print("the num is between 1 to 10")
    elif(num>10 and num<=20):
        print("the num is between 11 to 20")
    else:
        print("the num is greater than 20")    
else:
    ("the num is 0")






