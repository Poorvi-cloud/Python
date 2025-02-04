# TUPLES IN PYTHON
# tuples= it is similar to the list , but you cannot change it.

tup = (1,8,56,34,22)
print(type(tup), tup)
tup1=(1,) # u need to add comma at the end, otherwise it will something else
print(type(tup1), tup1)
print(tup[1])
print(tup[2])
if 56 in tup:
    print("yes")
tup2 = tup[1:4] # slicing will not change the tuple , it will make a new tuple
print(tup2) 
