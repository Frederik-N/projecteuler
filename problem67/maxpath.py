
# gammel løsning til et problem på projecteuler tl at løse problem67
data = open("p067_triangle.txt","r")
if(data.mode == 'r'):
    A = data.read()

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
    print(table)
    print(maxPath(table))