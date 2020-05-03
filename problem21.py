# Problem 21 on Amicable numbers
#
#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
#Evaluate the sum of all the amicable numbers under 10000.

import math

# funktion til at finde proper divisors af n
def d(n):
    sum = 1
    for m in range(2, int(math.sqrt(n))):
        if(n%m==0):
            if (m==(n/m)):
                sum += m 
            else:
                sum += (m + n/m)
    return sum

# loop til at evaluere sum af alle amicable numbers under 10000.
sumA = 0
amiclist = []
for n in range(0, 10000):
    m = d(n)
    calcdm = d(m)
    if(calcdm==n and d(n)==m and n != m):
        if(n not in amiclist and m not in amiclist):
            amiclist.append(n)
            amiclist.append(m)
            sumA += n + m
print(sumA)
