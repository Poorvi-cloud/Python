# # PYTHON LIST
marks = [3,4,5,"Poorvi",True, 0, 89, 90, 45,29]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])

print(marks[-3]) #negative index 
print(marks[len(marks)-3]) # positive index
print(marks[5-3]) # positive index
print(marks[2]) # positive index

if 7 in marks:
    print("yes")
else:
    print("no")

if "vi" in "Poorvi":
    print("yes")
else:
    print("no")
if "oor" in "Poorvi":
    print("yes .. haa")

#to print all the marks
print(marks)
print(marks[1:])  
print(marks[0:10])
print(marks[1:6:2])

#list comprehension
lst= [i for i in range (9) if i%2==0]
lst1= [i*i for i in range (7)]
lst2= [i*i for i in range (5)]
print(lst)
print(lst1)
print(lst2)
