#Write a program that asks for a sentence and prints the number of words on it. For example. "Hello world" should print 2.
print("welcome to the word counter MK3.2")
print("be aware that over spacing words will cause some problems")
name=input("please write a sentence: ")
x= " "
z=""
if x in name:
  name2=name.replace(x,z)
  #Here I erased all spaces between words and created name2
  #len() also counts spaces, so the difference of the lens is the quantity of spaces
  y=(len(name)-len(name2) +1)
  #The plus one is necessary because in every sentence like there is space less than words
  #like (I love tacos) or (I died) and even large texts
  print("there are",y,"words in this sentence")

else:
 print(name, "is just a single word" )
