# EXERCISE : Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. Here is a sample program and documentation link for you:
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

import time
a = input("Enter your name: ")
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
h = int(time.strftime("%H"))
if(h>4 and h<12):
    print("Good morning",a)
elif(h>12 and h<4):
    print("Good afternoon",a)
else:
    print("Good evening",a)