x=input("Please write a phrase: ")
Word_counter=x.count(' ')
#Here he counts the number of words -1, used on the index later which begins with 0
Word_list=x.split()
backup=x.split()
#This split commands finds some character of a string and split the phrase everytime it appears
#By splitting, it adds the separated parts into a list.
#If the split command is empty, he will split everyime " " appears.
j="*"
c=' '
i2=-1
def function(z):
  return len(z)
#def creates a function that do simple things and returns some kind of value
#I didn´t fully understood what should go in the parenthesis, but every letter works in this case,probably because of the key on sort.
Word_list.sort(key=function,reverse=True )
#Here he uses the len value to sort by the largest len number, but reversed.
a=(Word_list[0])
a=len(a)
i=0
#Basically the lar gest number is printed and this represents the "x" side of the square.
print(j*(a+4))
while i2<Word_counter:
 i2=i2+1
 subs=len(backup[i2])
 #Backup is used because the last list was modified and out of order.
 difference=(a-subs)
 #I made it print the difference multiplied by " " so the square becomes equal when the words are smaller.
 print(j+" "+backup[i2]+difference*c+" "+j)
 i=i+1
 if Word_counter<=i2:
  break
print(j*(a+4))
