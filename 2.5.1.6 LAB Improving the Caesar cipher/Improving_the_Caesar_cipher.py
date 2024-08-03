"""
Name        : Caesar cipher
Date        : 03/08/2024
Author      : Noureddine Bouyguir
Description : - improving the student's skills in operating with strings;
              - converting characters into ASCII code, and vice versa.
"""

text= input("Enter text to encrypt: ")
shift=int(input())
enc_text=""

if shift>=1 and shift<=25:
    for c in text:
        if c.isupper():
            enc_text += chr(ord(c)+shift) if ord(c)+shift <= ord("Z") \
                else chr(ord("A")+(shift-(ord("Z")-ord(c)+1)))
        elif c.islower():
            enc_text += chr(ord(c)+shift) if ord(c)+shift <= ord("z") \
                else chr(ord("a")+(shift-(ord("z")-ord(c)+1)))
        else:
            enc_text+=c

print(enc_text)


            
