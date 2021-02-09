#Write a program that asks a message and prints it in reverse order. As an example, HELLO WORLD should print DLROW OLLEH
x=input("please write a sentence and I´ll print it backyards ")
x=str(x)
c=0
z=""
d=0
while len(z)<len(x):
 c=c+1
 if d==0:
  y=x[-c:]
  d=d+1
  z=z+y
 elif d>0:
  y=x[-c:][:-d]
  d=d+1
  z=z+y
print(z)
