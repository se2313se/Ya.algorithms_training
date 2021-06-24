with open('input.txt', 'r', encoding='utf8') as f:
    values = list(map(int, f.readline().split()))
b = [values[i-1]<values[i] and values[i+1]<values[i] for i in range(1, len(values)-1)]
print(sum(b))
