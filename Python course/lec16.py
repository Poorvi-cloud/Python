# MATCH CASE STATEMENT

x = int(input("enter the value of x:"))
# x is the variable to match
match x:
    case 0:
        print("x is zero")
    case 1:
        print("x is 1")
    case 2:
        print(x)
    case _ if x!=90:
        print("x is not 90")
    case _ if x!=70:
        print("x is not 70")
