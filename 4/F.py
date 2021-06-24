def add(data, name, article, count):
    if name not in data:
        data[name] = {}
    if article not in data[name]:
        data[name][article] = 0
    data[name][article] += count


with open('input.txt', 'r', encoding='utf8') as f:
    data = {}
    for row in f.readlines():
        if row!='':
            name, article, count = list(row.split())
            count = int(count)
            add(data, name, article, count)

for name in sorted(data.keys()):
    print(name+':')
    for article in sorted(data[name].keys()):
        print(article, data[name][article])
