def check(k, a):
    if k == 1:
        return a[-2::-1]
    if a[-(k//2):] == a[-((k+1)//2)-1:-((k+1)//2 + k//2)-1:-1]:
        return a[-((k+1)//2 + k//2)-1::-1]
    return check(k-1, a)


with open('input.txt', 'r', encoding='utf8') as f:
    n = int(f.readline())
    v = list(map(float, f.readline().split()))
ans = check(n, v)
print(len(ans))
print(' '.join([str(int(_)) for _ in ans]))
