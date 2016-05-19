number = input("what is your number?")
d=2
factors =[]
while(number>1):
     while(number%d==0):
          factors.append(d)
          number=number/d
     d+=1
print max(factors)
          


