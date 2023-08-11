#
#%00
#%25         %30         %30
#%25 %32 %35 %25 %33 %30 %25 %33 %30
#↓↓↓
#%25         %32         %35         %25         %33         %30         %25         %33         %30
#%25 %32 %35 %25 %33 %32 %25 %33 %35 %25 %32 %35 %25 %33 %33 %25 %33 %30 %25 %32 %35 %25 %33 %33 %25 %33 %32



#Recursive encoding

import sys

A = 60 #seconds
a = 24 #hours
b = 12 #months
c = 365 #days
d = 1 #year
e = 2 #eternities
time = lambda x: x - x / x

def bang(p):
    D = 0
    E = ""
    F = []
    B = "%00"
    print(B)
    C = B
    while ( D <= p ):
        for letter in C:
            if letter == "%":
                E += "%25"
            if letter == "0":
                E += "%30"
            if letter == "2":
                E += "%32"
            if letter == "3":
                E += "%33"
            if letter == "5":
                E += "%35"
            F.append(D)
            timer = map(time, F)
        D += 1
        C = E
        print(C)
        E = ""
bang(A)
bang(a)
bang(b)
bang(c)
bang(d)
bang(e) 
        
with open("encoded.txt", "w") as f:
    f.write(C)
    
