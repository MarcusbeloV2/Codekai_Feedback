#Write a program that asks for list of comma-separated numbers and prints only the odd numbers.
number=input("Please write a list of numbers separated by commas: ")
i=-1
num=""
#num holds the str numbers that are picked from the list and empty itself after its job.
oddnumbers_list=[]
#This list is used to hold the odd numbers discovered and is printed in the end.
z=list(number)
#Thats the main list that we will be extracting the numbers that someone typed.
#Had to do one special case here because my temporizer conflicted with the max index on the main part of the code.
#Because of that, the last number didn´t appeared in the list, so the special case checks the last number on the list.
#This special case ended being larger than the main code, but it had to be done.
debug=-1
a=(z[debug])
#Here It picks up the last number on the list, I repeated this command because a is in the conditional, so I need to show what it is first
#Also, working with numbers and lists is horrible because the output from lists are one by one, they don´t recognize 100 by 100,but as 1,0,0.
#Basically he will be picking numbers from the last number and adding to num,until he found the comma.
#When a="," he will check if the number is odd and put it in oddnumbers_list.
while a!=",":
 a=(z[debug])
 #Here it picks the last thing in the list, probably a number, but not completely
 if a!=",":
   num=str(num)
   num=num+a
   debug=debug-1
   #Here it adds the number to the value num
 if a==",":
  num=num[::-1]
#[::-1] needs to be used because when picking each part of the number one by one, it ends by transforming Ex: (,213) into (312,)
#Obviously he don´t add the comma to num, because that would compromise the entire code and checking process.
  check=(int(num)*5)
  check=str(check)
  if check[-1:]=="5":
#My checking process was: every odd number *5 ends with 5 :)
#Here he adds num to the list if the check part is true, and num becomes empty again.
   oddnumbers_list.append(num)
   num=""
  else:
     num=""
#Believe it or not, but the main part of the code is below \(0o0)/
#Its kinda the same principle, but "i" controls the index and the conditional,but it can´t finish its job.
#it checks everything, with the exception of the last number, if I remove the +1 the max index is surpassed and an error occur.
while len(z)>i+1:
 i=i+1
 a=(z[i])
 if ','==a:
  num=int(num)
  check=num*5
  check=str(check)
  if check[-1:]=="5":
   oddnumbers_list.append(num)
   num=""
  else:
      num=""
 else:
    num=str(num)
    num=num+a
print(*oddnumbers_list, sep=",")
