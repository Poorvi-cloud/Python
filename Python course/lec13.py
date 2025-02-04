# UPPER CASE
# string are immutable
a = "poorvi"
print(len(a))
print(a.upper())
# LOWER CASE
print(a.lower())
# rstrip() removes the trailing characters
b = "poorvi!!!!!"
print(b.rstrip("!"))
# replace() replaces the String
print(a.replace("poorvi","vani"))
# split() method splits the given string at the specified instance and returns the seperated string
c="!!!poorvi!! !!!!! poorvi"
print(c.split(" ")) # space the inverted commas (" ")
#capatalize() method turns the first character of the string to uppercase and the rest other characters of the string are turned to the lower case.
d ="POOrvi is learning PYthON"
print(d.capitalize())
# center() method aligns the string to the center as per the parameters given by the user.
print(d.center(80))
#count() method returns the number of times the given value has occured within the given string.
print(c.count("poorvi"))
#endswith() method checks if the stirng ends with the given value. if yes then return true, else false.
print(b.endswith("!!!"))
print(b.endswith("o"))
# find() method searches for the first occurences of the given value and returns the index where it is present. if the given value is absent from the string then return -1.
print(d.find("learning"))
# The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.
print(d.index("is"))
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
print(d.isalnum())
# The isalpha() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.
e = "welcome"
print(e.isalpha())
# The islower() method returns True if all the characters in the string are lower case, else it returns False.
print(a.islower())
# The isprintable() method returns True if all the values within the given string are printable, if not, then return False
print(a.isprintable())
# The isspace() method returns True only and only if the string contains white spaces, else returns False.
a1 = "   i am a girl"
print(a1.isspace())
a2 = "       "
print(a2.isspace())
# The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
a3 = " Poorvi Will Be A Good Engineer"
print(a3.istitle())
a4 = "poorvi is a good GIRL"
print(a4.istitle())
# The isupper() method returns True if all the characters in the string are upper case, else it returns False.
b1 = "VANI IS MY SISTER"
print(b1.isupper())
# The startswith() method checks if the string starts with a given value. If yes then return True, else return False.
b2= "Poorvi and vani are sisters"
print(b2.startswith("Poorvi"))
# The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.
b3 = " MY FathEr is GrEat Man"
print(b3.swapcase())
# The title() method capitalizes each letter of the word within the string
b4= "i live in a nuclear family"
print(b4.title())








