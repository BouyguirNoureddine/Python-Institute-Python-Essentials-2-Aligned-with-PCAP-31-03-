"""
Name        : Anagrams
Date        : 03/08/2024
Author      : Noureddine Bouyguir
Description : - improving the student's skills in operating with strings;
              - converting strings into lists, and vice versa.
"""

text1=[c1.lower() for c1 in input().strip()]
text2=[c1.lower() for c1 in input().strip()]
res=0
for i in range(len(text1)):
    if text1[i] in text2:
        res+=1
print("Anagrams") if res==len(text1) and len(text1)>1 else print("Not anagrams")
