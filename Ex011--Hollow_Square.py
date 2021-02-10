
import random
a=random.randint(1,10)
c='*'
b=1
if a<=2:
 while b<a + 1:
  b=b+1
  print(a*c)
if a>3:
 e=' '
 print(a*c)
 while b<= a - 2:
     b=b+1
     print(c,e*(a-4),c)
 print(a*c)
if a==3:
 print(a*c)
 print("* *")
 print(a*c)
