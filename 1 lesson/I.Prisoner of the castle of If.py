with open('input.txt', 'r', encoding='utf8') as f:
    a, b, c, d, e = map(int, [line.strip() for line in f.readlines()])

if d>=a and e>=b or d>=b and e>=a:
    print('YES')
elif d>=b and e>=c or d>=c and e>=b:
    print('YES')
elif d>=c and e>=a or d>=a and e>=c:
    print('YES')
else:
    print('NO')
