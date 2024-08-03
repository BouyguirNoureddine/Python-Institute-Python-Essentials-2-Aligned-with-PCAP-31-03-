"""
Name        : Palindromes
Date        : 03/08/2024
Author      : Noureddine Bouyguir
Description : - improving the student's skills in operating with strings.
              - encouraging the student to look for non-obvious solutions.
"""

text=input()

text=text.lower().replace(" ","")
if text == text[-1:-len(text)-1:-1] and len(text)>1:
    print("It's a palindrome")
else:
    print("It's not a palindrome")