#DICTIONARY METHODS

d1= {233:56, 657:8, 786:3}
d2= {5611:78, 907:34, 3444:65, 676:31}
d1.update(d2)
print(d1)
#d1.clear()
#print(d1)
d1.pop(786)
print(d1)
d1.popitem()
print(d1)