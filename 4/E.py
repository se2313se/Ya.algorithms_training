with open('input.txt', 'r', encoding='utf8') as f:
    n = int(f.readline())
    blocks = []
    for i in range(n):
        blocks.append([-x for x in list(map(int, f.readline().split()))])
    blocks.sort()
    cur = None
    h = 0
    for x in blocks:
        if cur is None or x[0]>cur:
            cur = x[0]
            h+=x[1]
    print(-h)
