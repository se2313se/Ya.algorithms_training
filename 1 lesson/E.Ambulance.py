
with open('input.txt', 'r', encoding='utf8') as f:
    k1, m, k2, p2, n2 = map(int, f.readlines()[0].split())

if k2 // (m * (p2 - 1) + n2) < 1:
    print(-1, -1)
elif n2 == 1 and p2 == 1:  # n2 == 1 and k2 == 1:
    if k1 <= k2:
        print(1, 1)
    elif m == 1:
        print(0, 1)
    elif k1 <= k2*m:
        print(1, 0)
    else:
        print(0, 0)
elif k2**(1/2) >= n2:
    print(0, 0)
else:
    k = (k2-1)//(n2+m*(p2-1))+1
    p1 = ((k1//k-1)//m)+1
    n1 = k1//k - (p1-1)*m+1
    print(p1, n1)
