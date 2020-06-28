
# gammel løsning til et problem på projecteuler
def maxpathsolve():
    A = \
    '''
    75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
    '''

    n = len(A.strip().split('\n'))
    X = [[int(x) for x in row.split(' ')] for row in A.strip().split('\n')]

    #Zero Table
    table = []
    for i in range(n):
        row = []
        for j in range(2*n-1):
            row.append((0,0))
        table.append(row)        

    #Binary Tree Table
    s = n - 1
    for i,row in enumerate(table):
        k = s
        for z,j in enumerate(X[i]):
            table[i][s] = [j,None]
            s += 2
        s = k-1

    
    def maxPath(tab,i=0,j=n-1):
        if j < 0 or j > (2*n-1)-1 or i<0 or i > n-1:
            return 0
        
        m = tab[i][j][1]
        if m != None:
            return m
        
        l = maxPath(tab,i+1,j-1) +  tab[i][j][0]
        r = maxPath(tab,i+1,j+1) +  tab[i][j][0]

        tab[i][j][1] = max(l,r)
        return tab[i][j][1]


    if __name__ == "__main__":
        print(maxPath(table))