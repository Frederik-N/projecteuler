import numpy as np
import math
import sympy

def divisors(n):
    number_of_factors = 0
    for i in range(1, int(math.ceil(math.sqrt(n)))+1):
        if n % i == 0:
            number_of_factors +=2
        if i*i==n:
            number_of_factors -=1
    return number_of_factors

for n in range(1,1000000):
    Tn=(n*(n+1))/2
    if n%2==0:
        cnt=divisors(n/2)*divisors(n+1)
    else:
        cnt=divisors(n)*divisors((n+1)/2)
    if cnt >= 500:
        print (Tn)
        break