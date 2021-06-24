with open('input.txt', 'r', encoding='utf8') as f:
    a, b, c, d, e, f = map(int, [line.strip() for line in f.readlines()])

if a*b*c*d*e*f != 0:
    if a/c == b/d:
        if b/d == e/f:
            print(1, -a/b, e/b)
        else:
            print(0)
    else:
        y = (c*e-a*f)/(b*c-a*d)
        x = (f-d*y)/c
        print(2, x, y)
elif 1:
    1
