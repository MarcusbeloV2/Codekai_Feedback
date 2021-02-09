#Write a program that asks the user for a number n and prints the sum of the numbers 1 to n.
x=input("please write a number")
x=int(x)
if x==0:
 print("0 shouldn´t be used in this operation")
else:
 print((x + 1) * x /2)
