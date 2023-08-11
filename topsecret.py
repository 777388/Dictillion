#
#%00
#%25         %30         %30
#%25 %32 %35 %25 %33 %30 %25 %33 %30
#↓↓↓
#%25         %32         %35         %25         %33         %30         %25         %33         %30
#%25 %32 %35 %25 %33 %32 %25 %33 %35 %25 %32 %35 %25 %33 %33 %25 %33 %30 %25 %32 %35 %25 %33 %33 %25 %33 %32



#Recursive encoding

import sys

A = int(sys.argv[1])
B = "%00"
print(B)
C = B
D = 0
E = ""
F = []
time = lambda x: x - x / x

while ( D <= A ):
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
    
with open("encoded.txt", "w") as f:
    f.write(C)
    
