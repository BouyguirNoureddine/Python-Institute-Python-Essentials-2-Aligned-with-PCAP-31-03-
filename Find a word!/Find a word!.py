"""
Name        : Find a word!
Date        : 03/08/2024
Author      : Noureddine Bouyguir
Description : - improving the student's skills in operating with strings;
              - using the find() method for searching strings.
"""

text1=input()
text2=input()
res=0
for c in text1:
    if text2.find(c) != -1 :
        res+=1
if res==len(text1):
    print("Yes")
else:
    print("No")

