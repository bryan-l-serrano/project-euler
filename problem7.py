prime = [2]
x = 3
while x < 1000000:
     y = 2
     print x 
     while y <x:
          number = x % y
          if number != 0:
               y +=1
          if number == 0:
               y=2
               x +=1
               continue
               
     if y == x:
          prime.append(x)
          if len(prime)== 10001:
               print prime[10000]
               break
          else:
               
               x+=1

                    
                    
