empty = []
for x in range(1,1000):
     if x % 3 == 0:
          empty.append(x)
     elif x % 5 == 0 :
          empty.append(x)
     
print empty
print sum(empty)
