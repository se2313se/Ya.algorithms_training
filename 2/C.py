with open('input.txt', 'r', encoding='utf8') as f:
    n = int(f.readline())
    values = list(map(int, f.readline().split()))
    x = int(f.readline())
d = [(values[i]-x)**2 for i in range(n)]
print(values[d.index(min(d))])
