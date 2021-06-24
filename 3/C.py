with open('input.txt', 'r', encoding='UTF8') as f:
    n, m = map(int, f.readline().split())

    line1 = set([int(f.readline().strip()) for i in range(n)])
    line2 = set([int(f.readline().strip()) for i in range(m)])

    ans = [[] for i in range(3)]
    ans[0] = [a for a in line1 if a in line2]
    ans[1] = [a for a in line1 if a not in line2]
    ans[2] = [a for a in line2 if a not in line1]
    for a in ans:
        print(len(a))
        print(' '.join([str(_) for _ in sorted(a)]))
