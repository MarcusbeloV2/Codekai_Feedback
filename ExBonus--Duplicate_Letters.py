#Duplicate encoder, write a program that convert a string into a new string, where if a chacracter is unique it becomes "(" if not, it becomes ")"
x = input("Please write a word: ")
len1 = (len(x)-1)
#Here len1 will be used for index, which can´t have the same number as len because it starts with 0.
i2 = -1
i = -1
b = "pão"
token = "opa"
#'token' can be anything, but they must be something unusual at first in order to not compromise the code.
#After each check, the token will be set either to true or false, if true, the character is not unique.
finalword=[]
#finalword is the list that characters will be storaged,and will be printed once the conversion is over.
y=len(finalword)
#After each process I had to make sure to get the value of the elements in the list, so when it becomes the same as the input, the process must stop
opa=list(x)
#opa represents a list where all characters are separeted and represents elements.
while i<len1:
 i=i+1
 a=(opa[i])
 i2=-1
 y=len(finalword)
 if token=="false" and y<len(x):
  finalword.append("(")
 token="false"
 while i2<len1:
    i2=i2+1
    if i2!=i:
     b=(opa[i2])
     y=len(finalword)
    if a==b and i2!= i and y<len(x):
     token="true"
     finalword.append(")")
     break
y=len(finalword)
if token=="false" and y<len(x):
    finalword.append("(")

print(*finalword)
#The rest of the code is pretty simple itself, it will get every letter(represented by the first while)
#The second while will work by getting other letters and trying to see if any of them match.
#If not, the token, will be set to false and will add "(" to finalword.
#If a Duplicate letter is found, token will be set to true,")" will be added to finalword, and the loop will break,reseting the value of i and changing letters
#Breaking the loop is essencial, so it won´t continue adding ")" if more than 2 equal characters are found.
#I found this code worth studying, because there are a lot of small details that without them, the code wouldn´t work, such as line 27
