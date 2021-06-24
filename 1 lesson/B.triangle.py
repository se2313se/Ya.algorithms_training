sides = [float(input()) for i in range(3)]
sides = sorted(sides)
mark = False

if sides[0] * sides[1] * sides[2]:
    if sides[-1] < sum(sides[:2]):
        if sides[0] < sum(sides[1:3]):
            if sides[1] < sides[0] + sides[2]:
                print('YES')
                mark = True

if not mark: print('NO')
