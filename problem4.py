empty = []
empty2 =[]
h=0
n=0
for h in range(0,1000):
     for n in range(0,1000):
          answer = n*h
          answer = str(answer)
          if len(answer) == 6 and answer[0] == answer[5] and answer[1] == answer[4] and answer [2] == answer[3]:
               empty.append(answer)
          elif len(answer) ==5 and answer[0] == answer[4] and answer[1] == answer[3]:
               empty.append(answer)
          if len(answer) == 4 and answer[0] == answer[3] and answer[1] == answer[2]:
               empty.append(answer)
          elif len (answer) == 3 and answer[0] == answer[2]:
               empty.append(answer)
          elif len(answer) == 2 and answer[0] == answer[1]:
               empty.append(answer)
for strings in empty:
     if len(strings) == 6:
          empty2.append(strings)
for strings in empty2:
     strings = int(strings)
print empty2
print max(empty2)



