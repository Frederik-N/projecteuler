# gammel løsning til et problem på projecteuler

import numpy as np
import math
import scipy.special

sum = 2**1000
plussum = 0
sum = str(sum)

for c in sum:
    plussum += int(c)

print(plussum)
