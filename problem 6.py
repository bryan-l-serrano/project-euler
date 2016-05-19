sum_of_squares = []
square_of_sums = []
for x in range (0,101):
     square_of_sums.append(x)
     n = x *x
     sum_of_squares.append(n)
SQS = sum(square_of_sums)**2
SUMSQ = sum(sum_of_squares)
DIFF = SQS - SUMSQ
print SQS
print SUMSQ
print DIFF
