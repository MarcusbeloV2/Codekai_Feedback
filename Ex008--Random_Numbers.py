#Write a program that generates 6 different random numbers between 1 and 60 (included). 
import random
a=1
b=1
c=1
d=1
e=1
f=1
while 1+1==2:
 a=random.randint(1,60)
 b=random.randint(1,60)
 c=random.randint(1,60)
 d=random.randint(1,60)
 e=random.randint(1,60)
 f=random.randint(1,60)
 if a!=b:
  if a!=c:
   if a!=d:
    if a!=e:
     if a!=f:
      if b!=c:
       if b!=d:
        if b!=e:
         if b!=f:
          if c!=d:
           if c!=e:
            if c!=f:
             if d!=e:
              if d!=f:
               if e!=f:
                break


print(a,b,c,d,e,f)
