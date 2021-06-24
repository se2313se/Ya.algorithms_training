with open('input.txt', 'r', encoding='utf8') as f:
    a1, b1, a2, b2 = map(int, f.readlines()[0].split())

if min(a1, b1) == min(a2, b2):
    print(min(a1, b1), max(a1, b1) + max(a2, b2))
elif max(a1, b1) == min(a2, b2):
    print(min(a2, b2), min(a1, b1) + max(a2, b2))
elif min(a1, b1) == max(a2, b2):
    print(max(a2, b2), max(a1, b1) + min(a2, b2))
elif max(a1, b1) == max(a2, b2):
    print(max(a2, b2), min(a1, b1) + min(a2, b2))
elif min(a1, b1) > max(a2, b2):
    print(min(a1, b1), max(a1, b1) + min(a2, b2))
elif min(a1, b1) < max(a2, b2) < max(a1, b1):
    print(max(a1, b1), min(a1, b1) + min(a2, b2))
elif max(a1, b1) < max(a2, b2):
    print(max(a2, b2), min(a1, b1) + min(a2, b2))
