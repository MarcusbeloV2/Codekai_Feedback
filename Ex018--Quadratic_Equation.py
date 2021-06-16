#Write a program that receives the coefficients of a quadratic equation and writes its roots.
import math
print("all quadratic functions are like this: a(x.x)+bx+c")
print("In this program we solve them for u quickly :D")
a=int(input("please write the value of a: "))
b=int(input("please write the value of b: "))
c=int(input("please write the value of c: "))
Delta=(b**2)-(4*a*c)
if Delta>=0:
 Delta=math.sqrt(Delta)
 root1=((-b + (Delta)) /(2*a))
 root2=((-b - (Delta)) /(2*a))
 print("x1 =",root1,"and x2 =",root2)
else:
    print("this equation don´t have real roots")
#Not much to explain in this exercise, the only new thing is the square root function(math.sqrt)
#Pretty much self explanatory
