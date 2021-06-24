with open('input.txt', 'r', encoding='UTF8') as f:
    line1 = set(map(int, f.readline().split()))
    line2 = set(map(int, f.readline().split()))
    ans = [a for a in line1 if a in line2]

    print(' '.join([str(a) for a in line1 if a in line2]))
