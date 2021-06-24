with open('input.txt', 'r', encoding='UTF8') as f:
    print(len(set([a for line in f.readlines() for a in line.split()])))
