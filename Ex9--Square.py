#Write a program that generates a square of random size. Sizes must be between 1 and 10 (included).
import random
a=random.randint(0,9)
b=0
c='*'
while b<a + 1:
 b=b+1
 print(c + c*a)
