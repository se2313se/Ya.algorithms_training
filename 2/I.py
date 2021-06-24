with open('input.txt', 'r', encoding='utf8') as f:
    n, m, k = map(int, f.readline().split())
    c = [[0 for i in range(m)] for j in range(n)]
    for i in range(k):
        x, y = map(int, f.readline().split())
        c[x-1][y-1] = '*'
        if y>1 and x>1 and type(c[x-2][y-2]) == int: c[x-2][y-2] += 1
        if x>1 and type(c[x-2][y-1]) == int: c[x-2][y-1] += 1
        if y<m and x>1 and type(c[x-2][y]) == int: c[x-2][y] += 1
        if y>1 and type(c[x-1][y-2]) == int: c[x-1][y-2] += 1
        if y<m and type(c[x-1][y]) == int: c[x-1][y] += 1
        if x<n and y>1 and type(c[x][y-2]) == int: c[x][y-2] += 1
        if x<n and type(c[x][y-1]) == int: c[x][y-1] += 1
        if x<n and y<m and type(c[x][y]) == int: c[x][y] += 1

for i in range(len(c)):
    print(''.join([str(k)+' ' for k in c[i]]))
