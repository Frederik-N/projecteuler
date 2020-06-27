# gammel løsning til et problem på projecteuler

import numpy as np
import math
import scipy.special

stringx = []
for x in range(1,1001):
    stringx.append(str(x))

def singledigits(c, counter):
    if(c =="1"):
        counter += 3
    if(c =="2"):
        counter += 3
    if(c =="3"):
        counter += 5
    if(c =="4"):
        counter += 4
    if(c =="5"):
        counter += 4
    if(c =="6"):
        counter += 3
    if(c =="7"):
        counter += 5
    if(c =="8"):
        counter += 5
    if(c =="9"):
        counter += 4
    else:
        return counter
    return counter

def dobbeldigits(c, counter):
    if(c =="2"):
        counter += 6
    if(c =="3"):
        counter += 6
    if(c =="4"):
        counter += 5
    if(c =="5"):
        counter += 5
    if(c =="6"):
        counter += 5
    if(c =="7"):
        counter += 7
    if(c =="8"):
        counter += 6
    if(c =="9"):
        counter += 6
    else:
        return counter
    return counter

def teendigits(c, counter):
    if(c =="0"):
        counter += 3
    if(c =="1"):
        counter += 6
    if(c =="2"):
        counter += 6
    if(c =="3"):
        counter += 8
    if(c =="4"):
        counter += 8
    if(c =="5"):
        counter += 7
    if(c =="6"):
        counter += 7
    if(c =="7"):
        counter += 9
    if(c =="8"):
        counter += 8
    if(c =="9"):
        counter += 8
    else:
        return counter
    return counter



def foo(s):
    counter = 0
    for c in s:
        listc = list(c)
        if(len(c)>0):
            print(listc)
            if(len(c)==4):
                counter += 11
            if(len(c)==3):
                element1 = listc.pop(len(c)-1)
                element2 = listc.pop(len(c)-2)
                if(element1!="0" or element2 !="0"):
                    counter += 3
                if(element2=="1"):
                    counter = teendigits(element1,counter)
                else:
                    counter = singledigits(element1, counter)
                    counter = dobbeldigits(element2, counter)
                element3 = listc.pop(len(c)-3)
                counter += 7
                counter = singledigits(element3, counter)

            if(len(c)==2):
                element1 = listc.pop(len(c)-1)
                element2 = listc.pop(len(c)-2)
                if(element2=="1"):
                    counter = teendigits(element1,counter)
                else:
                    counter = singledigits(element1, counter)
                    counter = dobbeldigits(element2, counter)
            if(len(c)==1):
                element = listc.pop(0)
                counter = singledigits(element, counter)
            print(counter)
    return counter

print(foo(stringx))
