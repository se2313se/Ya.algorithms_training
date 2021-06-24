with open('input.txt', 'r', encoding='utf8') as f:
    n = int(f.readline())
    values = list(map(float, f.readline().split()))
p = 0
v = 0
places = sorted(values, reverse=True)
for i in range(values.index(places[0])+1, n-1):
    if values[i]%10 == 5 and values[i]>values[i+1] and values[i]>v:
        v = values[i]
        p = places.index(v)+1
print(p)
