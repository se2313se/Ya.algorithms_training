values = list(map(float, input().split()))
s = [values[i] > values[i - 1] for i in range(1, len(values))]
print('YES' * all(s) + 'NO' * (not all(s)))



