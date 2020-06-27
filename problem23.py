# Problem 23 - Non-abundant sums
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
#  For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
#  By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
# However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number
#  that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import math

def abundantNumbers():
    abundantdivisors = []

    for number in range(1, 28123):
        listofdivisors = []
        i = 1
        while i <= math.sqrt(number):
            if(number % i == 0): 
                if(number / i == i):
                    listofdivisors.append(i)
                else:
                    listofdivisors.append(i)
                    listofdivisors.append(number/i)
            i = i + 1
        if number in listofdivisors:
            listofdivisors.remove(number)
        #print(int(sum(listofdivisors)), number)
        if(int(sum(listofdivisors))>number):
            abundantdivisors.append(number)
    # return the list up abundant divisors up to 28123
    return abundantdivisors

# traverses the abundantnumbers list and checks if there are two numbers in the list that gives n (bottleneck time complexity)
def isSumOfTwoAbundant(n, abundantNumbers):
    l = 0
    r = len(abundantNumbers)-1
    while(l<=r):
        if(abundantNumbers[l] + abundantNumbers[r] == n):
            return 1
        elif(abundantNumbers[l] + abundantNumbers[r] < n):
            l += 1
        else:
            r -= 1
    return 0


# Iterate through all numbers up to 28123 and check if it can be made from adding two abundant divisors from the list given by abundantNumber()
abundantNumbers = abundantNumbers()
result = []
for x in range(1,20162):
    if not(isSumOfTwoAbundant(x,abundantNumbers)):
        result.append(x)

print(sum(result))

