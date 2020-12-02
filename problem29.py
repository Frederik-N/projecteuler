# problem 29
import math

def solution():
    listnumbers = []
    for a in range(2, 101):
        for b in range(2, 101):
            listnumbers.append(math.pow(a,b))
    print(len(list( dict.fromkeys(listnumbers) )))
            

    

if __name__ == "__main__":
    solution()