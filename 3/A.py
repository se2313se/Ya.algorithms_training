with open('input.txt', 'r', encoding='utf8') as f:
    print(len(set(map(int, f.readline().split()))))
