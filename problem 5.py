empty = []
n = 1
while len(empty) == 0:
     print n
     x = 1
     while x <21:
          if n % x == 0:
               x += 1
               if x == 21:
                    empty.append(n)
          elif n % x != 0:
               break
     n += 1

print empty
