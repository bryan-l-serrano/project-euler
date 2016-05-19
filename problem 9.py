a= 0
b =1
c = 1
while a + b+ c != 1000:
     a+=1
     b=1
     for x in range(0,1000):
          b+=1
          c = (a**2 + b**2)** .5
          if a+ b+ c == 1000:
               break
print a*b*c

