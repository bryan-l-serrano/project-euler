empty =[]
for n in range(0,33):
     if n == 0:
          empty.append(1)
     elif n ==1:
          empty .append(1)
     else:
         M = empty[n-2] + empty[n-1]
         empty.append(M)
print empty
empty2 = [ x for x in empty if x %2 == 0]
print empty2
print sum(empty2)
