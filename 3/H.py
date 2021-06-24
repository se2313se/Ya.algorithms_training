with open('input.txt', 'r', encoding='UTF8') as f:
    n = int(f.readline().strip())
    coord = [list(map(int, f.readline().strip().split())) for i in range(n)]
    birds = [[i, coord[i][0], coord[i][1], coord[i][1]/coord[i][0]] for i in range(n)]
    birds.sort(key=lambda x: x[3], reverse=True)
    shots = 1
    tgs = set([birds[0][3]])
    xs = set([birds[0][1]])
    for i in range(1, n):
        if birds[i][1] not in xs:
            shots += 1
            xs.add(birds[i][1])
    print(shots)

