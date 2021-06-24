def create_blanc(s):
    alphabet = set(s)
    return {s: 0 for s in alphabet}


def check():
    with open('input.txt', 'r', encoding='utf8') as f:
        g, s = map(int, f.readline().split())
        w = f.readline().strip()
        S = f.readline().strip()
    w_voc = create_blanc(S)
    for _ in w:
        w_voc[_] += 1
    if g > s:
        return 0
    temp = create_blanc(S)
    cnt = 0
    for i in range(g):
        temp[S[i]] += 1
    if w_voc == temp:
        cnt += 1
    for i in range(g, s):
        temp[S[i-g]] -= 1
        temp[S[i]] += 1
        if w_voc == temp:
            cnt += 1
    return cnt


def check1():
    with open('input.txt', 'r', encoding='utf8') as f:
        g, s = map(int, f.readline().split())
        if g > s:
            return 0
        w = f.readline().strip()
        S = f.readline().strip()
    cnt = 0
    w = sorted([_ for _ in w])
    temp = [_ for _ in S[:g]]
    if sorted(temp) == sorted(w):
        cnt += 1
    for i in range(g, s):
        temp.pop(temp.index(S[i-g]))
        temp.append(S[i])
        if sorted(temp) == sorted(w):
            cnt += 1
    return cnt


print(check())
