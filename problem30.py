# problem 30
import math

def solution():
    listnumbers = []
    for n in range(1, 1000000):
        stringn = str(n)
        a,b,c,d,e,f,g,h,i = 0,0,0,0,0,0,0,0,0
        a = math.pow(int(stringn[0]), 5)
        if (len(stringn)>1):
            b = math.pow(int(stringn[1]), 5)
        if (len(stringn)>2):
            c = math.pow(int(stringn[2]), 5)
        if (len(stringn)>3):
            d = math.pow(int(stringn[3]), 5)
        if (len(stringn)>4):
            e = math.pow(int(stringn[4]), 5)
        if (len(stringn)>5):
            f = math.pow(int(stringn[5]), 5)
        if (len(stringn)>6):
            g = math.pow(int(stringn[6]), 5)
        if (len(stringn)>7):
            hasattr = math.pow(int(stringn[7]), 5)
        if (len(stringn)>8):
            i = math.pow(int(stringn[8]), 5)
        
        if (a + b + c + d+e+f+g+h+i == n):
            print(stringn, a, b, c, d,e,f,g,h,i, a+b+c+d+e+f+g+h+i)
            listnumbers.append(n)
    print(listnumbers)
    print(sum(listnumbers)-1)
            

    

if __name__ == "__main__":
    solution()