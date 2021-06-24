with open('input.txt', 'r', encoding='UTF8') as f:
    n = int(f.readline().strip())
    first = [f.readline().strip() for i in range(int(f.readline().strip()))]
    all = set(first)
    any = set(first)
    for j in range(n-1):
        temp = [f.readline().strip() for i in range(int(f.readline().strip()))]
        any = any.union(set(temp))
        all = all.intersection(set(temp))
    print(len(all))
    for i in range(len(all)):
        print(list(all)[i])
    print(len(any))
    for i in range(len(any)):
        print(list(any)[i])
