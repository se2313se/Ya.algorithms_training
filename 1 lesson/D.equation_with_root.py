a = float(input())
b = float(input())
c = float(input())  # = map(int, input().split())
mark = True
x = None
if c < 0:
    mark = False
elif a == 0:
    if not b == c ** 2:
        mark = False
else:
    if (c * c - b) / a == (c * c - b) // a:
        x = (c * c - b) / a
    else:
        mark = False

if x is None:
    print(mark * 'MANY SOLUTIONS' + (not mark) * 'NO SOLUTION')
else:
    print(int(x))
