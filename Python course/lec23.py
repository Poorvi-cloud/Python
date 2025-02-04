# LIST METHODS

lst= [1,5,6,3, 56,23, 90, 1, 1, 65,190, 7] 
print(lst)
lst.append(100) # we can add an element in the list with the help of a list method "append"
print(lst)
lst.sort() # we can sort the elements in the list with " sort "
print(lst)
lst.sort(reverse=True) # it reverses the order
print(lst)
lst.reverse() # reverses the order
print(lst)
print(lst.index(100)) # prints the occurence of the element
print(lst.count(1)) # it prints how many times the no. is repeated
m= lst.copy() # it copies the list and modifies the element of other list
m[0] = 0
print(m)
lst.insert(1, 233) # inserts the value at the place you want it to be get inserted
print(lst)
s = [ 192, 670, 458]
k = lst + m # it ads two list
print(k)
lst.extend(s) # it extends the list and add that list into the another list
print(lst)

