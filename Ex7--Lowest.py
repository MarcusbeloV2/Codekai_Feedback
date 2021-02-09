#Write a program that receives 3 numbers and prints the lowest of them
print("welcome to the number comparator MK3V2")
print("you will send us 3 numbers and I will send u the lowest")
x=int(input("please send the first number "))
y=int(input("please send the secound number"))
z=int(input("please send the third number"))
if x==y==z:
    print(x,"=",y,"=",z, "all numbers are equal", "so none is the lowest")
if x<y:
 if x<z:
  print(x,"is the lowest number")
 if z==x:
    print(x, "and", z,"are the lowest", "while",y,"is the largest")
if y<z:
 if y<x:
  print(y,"is the lowest number")
 if y==x:
    print(x, "and", y,"are the lowest", "while",z,"is the largest")
if z<x:
 if z<y:
  print(z,"is the lowest number")
 if z==y:
   print(y, "and", z,"are the lowest", "while",x,"is the largest")
