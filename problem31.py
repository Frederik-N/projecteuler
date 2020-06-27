# Problem 31 - Coin sums
#How many different ways can £2 be made using any number of coins?
#1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

# manual added 200p
result = 1

start = 0
cent1 = 0
cent2 = 0
cent5 = 0
cent10 = 0
cent20 = 0
cent50 = 0
cent100 = 0

for x in range(0,3):
    cent100 = x
    start = cent1 * 1 + cent2 * 2 + cent5 * 5 + cent10 * 10 + cent20 * 20 + cent50 * 50 + cent100 * 100
    if(start==200):
        result += 1
        break
    for y in range(0,5):
        cent50 = y
        start = cent1 * 1 + cent2 * 2 + cent5 * 5 + cent10 * 10 + cent20 * 20 + cent50 * 50 + cent100 * 100
        if(start==200):
            result += 1
            break
        for z in range(0, 11):
            cent20 = z
            start = cent1 * 1 + cent2 * 2 + cent5 * 5 + cent10 * 10 + cent20 * 20 + cent50 * 50 + cent100 * 100
            if(start==200):
                result += 1
                break
            for c in range(0, 21):
                cent10 = c
                start = cent1 * 1 + cent2 * 2 + cent5 * 5 + cent10 * 10 + cent20 * 20 + cent50 * 50 + cent100 * 100
                if(start==200):
                    result += 1
                    break
                for a in range(0, 41):
                    cent5 = a
                    start = cent1 * 1 + cent2 * 2 + cent5 * 5 + cent10 * 10 + cent20 * 20 + cent50 * 50 + cent100 * 100
                    if(start==200):
                        result += 1
                        break
                    for b in range(0, 101):
                        cent2 = b
                        start = cent1 * 1 + cent2 * 2 + cent5 * 5 + cent10 * 10 + cent20 * 20 + cent50 * 50 + cent100 * 100
                        if(start==200):
                            result += 1
                            break
                        for d in range(0, 201):
                            cent1 = d
                            start = cent1 * 1 + cent2 * 2 + cent5 * 5 + cent10 * 10 + cent20 * 20 + cent50 * 50 + cent100 * 100
                            if(start==200):
                                result += 1
                            if(start > 200):
                                break
            print(result, cent1, cent2, cent5,cent10, cent20, cent50, cent100)
print(result)
