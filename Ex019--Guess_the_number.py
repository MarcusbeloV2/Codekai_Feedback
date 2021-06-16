#Write a guessing game where the user has to guess a secret numberi between 1 and 100. After every guess the program tells the user whether their number was too large or too small. At the end the number of tries needed should be printed.
import random
import time
number=random.randint(1,100)
tries=0
print("Welcome to Guess the number!")
time.sleep(2)
print("This program will select a number between 1 and 100")
time.sleep(2)
print("Your objective is to guess it by luck")
time.sleep(2)
print("Don´t worry, it´s not that hard, we will also give you many hints :) ")
time.sleep(2)
print("Unless you choose hard mode :O ")
time.sleep(2)
print("the number has already been selected!")
time.sleep(2)
print("what about it?, wanna try? ")
gamemode=input("Please type 1 for normal mode or 2 for hard mode: ")
a=("1","2")
number=random.randint(1,100)
i=1
if gamemode not in a:
  print("please choose a viable option next time, game over for u :D ")
if gamemode==str(1):
   while i==1:
    guess=int(input("Try to guess it, type a number!: "))
    if guess>number:
     tries=tries+1
     print("The number you typed is higher, try again!")
     if guess-number in range(32, 102):
      print("That was far from the chosen number man, like, really far, try a lower one instead :)")
     if guess-number in range(12,31):
      print("Hmmm, its kinda close, try lowering the number")
     if guess-number in range(2,11):
      print("WOW!, THAT WAS CLOSE!")
    if guess<number:
     tries=tries+1
     print("The number you typed is lower, try again!")
     if number-guess in range(32, 102):
      print("That was far from the chosen number man, like, really far, try a higher one instead :)")
     if number-guess in range(12,31):
      print("Hmmm, its kinda close, try typing a higher number")
     if number-guess in range(2,11):
      print("WOW!, THAT WAS CLOSE!")
    if guess==number:
        tries=tries+1
        print("Congrats!! You guessed the right number!")
        time.sleep(2)
        print("You guessed the number in your",tries,"time guessing !")
        time.sleep(2)
        print("You should try hard mode, we won´t be giving you many hints \(OoO)/ )")
        i=2
if gamemode==str(2):
 print("I guess you are brave enough for a challenge")
 print(number)
 time.sleep(2)
 print("You are going to have a bad time, unless you are extremely lucky hehehe")
 time.sleep(2)
 print("If you get closer we will tell you, but it´s not as easy as normal mode ")
 while i==1:
  guess=int(input("Try to guess it, type a number!: "))
  tries=tries+1
  if guess!=number and (guess-number) not in range(1,16) and (number-guess) not in range(1,16):
   print("You got it very wrong, and there is no easy hints this mode :D ")
  if (guess-number) in range(1,16) or (number-guess) in range(1,16):
    print("Hey, the number you guessed is 15 numbers or less different than the correct one hehehe")
  if guess==number:
   print("Yooooo, you actually got it, I´m impressed")
   time.sleep(2)
   print("Real warriors choose the hardest path, and I´m proud of you!")
   time.sleep(2)
   print("Only took you",tries,"times to guess it right :P ")
   print("Now go brag to everybody that you won a hard game and thank you for playing S2")
   i=2
#I had a lot of fun programming this game, but just like ex18, there isn´t anything special to learn about it
#Pretty much self explanatory too
