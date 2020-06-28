# Problem 25 - Reciprocal cycles
#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part

d = 0
largestcycle = 0

# find the divison of m and n, finding cycles
def divide(m, n):
    quotient, c = str(m // n) + ".", 10 * (m % n)
    while c and c < n:
        c *= 10
        quotient += "0"
    digits = ""
    passed = {}
    i = 0
    while True:
        if c in passed:
            prefix = digits[:passed[c]]
            cycle = digits[passed[c]:]
            result = quotient + prefix + "(" + cycle + ")"

            global largestcycle
            if(int(cycle) > largestcycle):
                largestcycle = int(cycle)
                global d
                d = n 

            return result.replace("(0)", "").rstrip(".")
        q, r = c // n, c % n
        passed[c] = i
        digits += str(q)
        i += 1
        c = 10 * r

for x in range(2,1000):
    divide(1,x)
print(d)