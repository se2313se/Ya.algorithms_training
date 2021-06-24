with open('input.txt', 'r', encoding='UTF8') as f:
    buttons = set(f.readline().split())
    print(len(set([_ for _ in f.readline().strip() if _ not in buttons])))
