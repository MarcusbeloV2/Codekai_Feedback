#Write a program that generates a triangle of random size. Sizes must be between 1 and 50 (included)
import random
b=random.randint(2,51)
str = "*"
for i in range(1,b):
 print(i*str)
