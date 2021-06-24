with open('input.txt', 'r', encoding='UTF8') as f:
    n = int(f.readline().strip())
    c = []
    for i in range(n):
        a1, a2 = map(int, f.readline().strip().split())
        if (a1+a2 == n-1) and (a1*a2 > -1):
            if a1 not in c:
                c.append(a1)
    print(len(set(c)))
