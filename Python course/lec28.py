#f-strings in python

letter="Hello, my name is {}, and i am from {}"
name="Poorvi"
country="India"
#print(letter.format(name,country))

# use of fstring in python
print(f"Hello, my name is {name}, and i am from {country}")
price = 4.8976
text = (f"for only, {price:.2f} dollars")
print(text)
#print(text.format(price=9.7546424))