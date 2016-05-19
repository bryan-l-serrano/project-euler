primes = [2,3,5]
y = 0
for x in range(6,2000001):
     while y < len(primes):
          if x % primes[y] == 0:
               break
          if y == len(primes)-1:
               primes.append(x)
          y +=1
     y = 0
print sum(primes)
