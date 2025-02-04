#exercise

import random
import string

def reverse(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s
    
def get_random():
    rand=""
    for i in range(3):
        rand = rand+random.choice(string.ascii_lowercase)
    return rand   

def code(a):    
    if(len(a)<3):
        a=reverse(a)
    else:
        a=get_random()+a[1:]+a[0:1]+get_random()
    return a 
    
def decode(a):
    if(len(a)<3):
        a=reverse(a)
    else:
        a=a[3:-3]
        a=a[-1]+a[0:-1]
    return a
    
def codStr(a):
    b=a
    coded=""
    while True:
        j=b.find(" ")
        str=b[:j]
        coded=coded+code(str)+" "
        b=b[j+1:]
        
        if(b.find(" ")==-1):
          coded=coded+code(b)
          break
    return coded  
    
def decodStr(a):
    b=a
    decoded=""
    while True:
        j=b.find(" ")
        str=b[:j]
        decoded=decoded+decode(str)+" "
        b=b[j+1:]
        
        if(b.find(" ")==-1):
          decoded=decoded+decode(b)
          break
    return decoded      
        
    
while True:
    a=input('enter your message: ')
    b=int(input("enter 1 to lock, 2 to unlock: "))
    if (b==1):
        print("locked message: ",codStr(a))
    elif (b==2):
        print("unlocked message: ",decodStr(a))
    else:
        print("invalid. exiting")
        break