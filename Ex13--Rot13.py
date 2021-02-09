#Write a program that receives a message and encrypts it using ROT13 cipher
import string
b=input("please write a message ")
b=str(b)
a=string.ascii_lowercase
c=string.ascii_uppercase
d=("nopqrstuvwxyzabcdefghijklm")
e=("NOPQRSTUVWXYZABCDEFGHIJKLM")
f=b.maketrans(a,d)
g=b.maketrans(c,e)
h=b.translate(f)
print(h.translate(g))
