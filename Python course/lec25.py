# OPERATIONS ON TUPLE

# tuples r immutable , if u wanna change the tuple u need to convert it in the list 1st
tup = ("Germany", "India", "China", "America")
temp = list(tup)
temp.append("Russia")
print(temp)
temp.pop(3) # it deletes the element
print(temp)
temp[2]="Finland" # it adds the value where u wanna add
print(temp)
tuple = (23, 34, 78, 23, 23, 23)
poo = tuple.count(23)
print("count of 23 is:", poo)

# many more methods like insex, reverse, sort can be used in the tuple also ... just like list.
# all u need to remember is .. u need to change the tuple into the list 