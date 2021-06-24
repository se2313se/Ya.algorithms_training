with open('input.txt', 'r', encoding='utf8') as f:
    a, b, n, m = map(int, [line.strip() for line in f.readlines()])

mina = n + (n-1) * a
maxa = n*(a+1)+a
minb = m + (m-1) * b
maxb = m * (b+1)+b
# print(mina, maxa, minb, maxb)
if max(mina, maxa) < min(minb, maxb) or min(mina, maxa) > max(minb, maxb):
    print(-1)
else:
    print(max(mina, minb), min(maxa, maxb))
