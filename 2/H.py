with open('input.txt', 'r', encoding='utf8') as f:
    v = list(map(int, f.readline().split()))
v.sort()
if len(v) == 3:
    print(' '.join([str(v[i]) for i in range(3)]))
else:
    print((' '.join([str(j) for j in v[:2]])+' '+str(v[-1]))*(v[0]*v[1]*v[-1]>v[-1]*v[-2]*v[-3]) +
          ' '.join([str(j) for j in v[-3:]])*(not v[0]*v[1]*v[-1]>v[-1]*v[-2]*v[-3]))
