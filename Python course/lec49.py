# PILE IO IN PYTHON

f = open("main.txt", 'r')
print(f)
text = f.read()
print(text)
f.close()

p = open("main.txt", 'w')
print(p)
p.write(" you are awesome")
p.close()
