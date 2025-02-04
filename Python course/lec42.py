#ENUMERATE FUNCTION IN PYTHON

marks = [1,45,67,34,98,92,12,90]
'''index=0
for mark in marks:
    print(mark)
    if(index==3):
        print("hello")
    index +=1'''
for index, mark in enumerate(marks):
    print(mark)
    if (index==3):
        print("just passed")