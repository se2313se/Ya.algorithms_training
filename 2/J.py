with open('input.txt', 'r', encoding='utf8') as f:
    n = int(f.readline())
    prev = float(f.readline())
    high = 4000
    low = 30
    for i in range(1, n):
        temp = f.readline().split()
        cur, flag = float(temp[0]), temp[1]
        if cur - prev > 0:
            if flag == 'further':
                if (cur+prev)/2 < high:
                    high = (cur+prev)/2
            else:
                if (cur+prev)/2 > low:
                    low = (cur+prev)/2
        if cur - prev < 0:
            if flag == 'further':
                if (cur+prev)/2 > low:
                    low = (cur+prev)/2
            else:
                if (cur+prev)/2 < high:
                    high = (cur+prev)/2
        prev = cur
    print(low, high)
