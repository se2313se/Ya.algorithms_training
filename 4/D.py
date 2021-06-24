with open('input.txt', 'r', encoding='utf8') as f:
    keys = dict()
    n = int(f.readline())
    c = list(map(int, f.readline().split()))
    for i in range(n):
        keys[i+1] = c[i]
    k = int(f.readline())
    taps = list(map(int, f.readline().split()))
    for i in range(k):
        keys[taps[i]] -= 1
    for i in range(n):
        print('YES'*(keys[i+1]<0)+'NO'*(keys[i+1]>=0))
