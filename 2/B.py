with open('input.txt', 'r', encoding='utf8') as f:
    # a, b, c, d, e = map(int, [line.strip() for line in f.readlines()])
    const = []
    asc = []
    wasc = []
    desc = []
    wdsc = []
    rand = []
    prev = float(f.readline())
    n = float(f.readline())
    while n != -2e+9:
        const.append(n == prev)
        asc.append(n > prev)
        wasc.append(n >= prev)
        desc.append(n < prev)
        wdsc.append(n <= prev)
        prev = n
        n = float(f.readline())
    print(
        all(const)*'CONSTANT' +
        (all(asc) and not any(const))*'ASCENDING' +
        (all(wasc) and any(const) and not all(const))*'WEAKLY ASCENDING' +
        (all(desc) and not any(const))*'DESCENDING' +
        (all(wdsc) and any(const) and not all(const))*'WEAKLY DESCENDING' +
        (not (all(const)+all(asc)+all(wasc)*(not all(const))+all(desc)+all(wdsc)*(not all(const))))*'RANDOM'
    )
