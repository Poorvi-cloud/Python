#IMPORT FUNCTION IN PYTHON

import math
result = math.sqrt(9)
print(result)

#FROM = if u want to import only one method in the code, u can 'from'.

from math import sqrt,pi
r = sqrt(9)*pi
print(r)

# " import *" will add all the function and variable.

from math import *
a=sqrt(8)*pi
print(a)

# "as keyword"

from math import sqrt as p
b= p(7)
print(b)

#"dir function"

import math
print(dir(math))