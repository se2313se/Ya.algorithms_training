def operation(N, dc):
    if k<m:
        return 0
    temp = N - (N // k) * k
    dc += (N//k)*(k//m)
    temp += (N // k) * (k - (k//m) * m)
    if temp//k > 0:
        return operation(temp, dc)
    return dc


with open('input.txt', 'r', encoding='utf8') as f:
    n, k, m = map(int, f.readlines()[0].split())
c = 0
print(operation(n, c))
