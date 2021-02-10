#Write a program that asks for an integer and then prints it in binary format
x=int(input("please print an number so I´ll put in binary form"))
if x>0:
 print(bin(x)[2:])
if x<0:
 print( " -",bin(x)[3:])
