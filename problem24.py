# Problem 24 - Lexicographic permutations
#A permutation is an ordered arrangement of objects. 
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
# The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# does a lixicographic permutation on the digits n

# Function to find permutations of a given string 
from itertools import permutations 

# Get all permutations of string '0123456789' and get index of millionth permutation
string = "0123456789"
permList = permutations(string) 
print(list(permList)[999999])