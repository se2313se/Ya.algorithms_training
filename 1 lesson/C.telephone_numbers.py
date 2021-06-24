def number_cor(n):
    rtemp = ''
    for _ in n:
        if _.isdigit(): rtemp += _
    # rtemp = ''.join([c for c in phone if c.isdigit()])
    if len(rtemp) == 11:
        rtemp = '7' + rtemp[1:]
    elif len(rtemp) == 7:
        rtemp = '7495' + rtemp
    return rtemp


r0 = input()
r0 = number_cor(r0)

for i in range(3):
    r = input()
    r = number_cor(r)
    print('YES' * (r == r0) + 'NO' * (not r == r0))

