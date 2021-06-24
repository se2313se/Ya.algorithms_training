with open('input.txt', 'r', encoding='utf8') as f:
    v = list(map(int, f.readline().split()))
v.sort()
print(' '.join([str(j) for j in v[:2]])*(v[0]*v[1]>v[-1]*v[-2]) +
      ' '.join([str(j) for j in v[-2:]])*(not v[0]*v[1]>v[-1]*v[-2]))

