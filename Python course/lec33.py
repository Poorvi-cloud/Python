#PYTHON DICTIONARIES

dic = {
    "Name":"poorvi",
    "age":"20",
    "Field":"IT"
}
print(dic["Field"])
info = {'name':'poorvi', 'age':20, 'gender':'female'}
print(info)
print(info.values())
print(info.keys())
for keys in info.keys():
    print( f"the value of the keys {keys} is {info[keys]}")