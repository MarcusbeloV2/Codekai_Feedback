#Write a program that asks for a number n and prints the first n fibonacci numbers (see https://en.wikipedia.org/wiki/Fibonacci_number). As an example, if n = 6 the program should print 1,1,2,3,5,8
num=int(input("please write a number: "))
a=1
b=0
i=0
fibonnaci_list=[]
#here I created a list to put every result of a and b
while i<=num:
 a=(a+b)
 #First he prints 1 and the a value doesn´t change
 #The append command is only used on lists and he adds a string value to a list
 fibonnaci_list.append(str(a))
 i=i+1
 #i increase by one everytime a value enters the list
 if i>=num:
  break
 b=(b+a)
 fibonnaci_list.append(str(b))
 i=i+1
 if i>=num:
  break
print(*fibonnaci_list, sep=",")
#The "*" is used to output everything from the list spaced
#The sep command is used together with print to separate each value in a certain way
