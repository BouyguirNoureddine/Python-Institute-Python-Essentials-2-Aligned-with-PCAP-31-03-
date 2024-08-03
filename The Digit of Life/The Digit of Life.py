"""
Name        : The Digit of Life
Date        : 03/08/2024
Author      : Noureddine Bouyguir
Description : - improving the student's skills in operating with strings;
              - converting integers into strings, and vice versa.
"""

b_date=input("Enter birthday (in the format YYYYMMDD): ")
sums1,sums2=0,0
for c in b_date:
    sums1+=int(c)
if len(str(sums1))>1:
    for c in str(sums1):
        sums2+=int(c)
else:
    sums2=sums1
print(sums2)