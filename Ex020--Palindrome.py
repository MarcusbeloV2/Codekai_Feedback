#Write a program that takes a sentence as input and writes whether it is a palindrome or not. A palindrome is string that matches to it self when reversed (not counting spaces).
eraser=""
target=" "
message=input("Please write a message: ")
inverted=message[::-1]
final=inverted.replace(target,eraser)
message2=message.replace(target,eraser)
if message2==final:
 print(message,"is a palindrome")
else:
 print(message,"is not a palindrome")
