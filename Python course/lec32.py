#JOINING SETS

s1={2,4,1,3}
s2={4,8,6,5,4}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)

c1={"Delhi","Vadodara","Agra", "Anand"}
c2={"Pune", "Mumbai", "Ahmedabad", "Nadiad", "Delhi", "Vadodara"}
print(c1.difference(c2))
print(c1.intersection(c2))
print(c1.symmetric_difference(c2))
print(c1.isdisjoint(c2))
print(c1.issuperset(c2))
c1.add("Kolkata")
print(c1)
c1.remove("Kolkata")
print(c1)
item = c1.pop
print(c1)
print(item)
del(c1)
print(c1)