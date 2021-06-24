with open('input.txt', 'r', encoding='UTF8') as f:
    line1 = f.readline().strip()
    line2 = f.readline().strip()
    line2 = set([line2[i:i+2] for i in range(len(line2)-1)])
    c = 0
    for i in range(len(line1) - 1):
        if line1[i:i + 2] in line2:
            c += 1
    print(c)

