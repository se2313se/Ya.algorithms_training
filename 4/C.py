inFile = open('input.txt', 'r', encoding='utf8')
inFileLines = inFile.readlines()
words = dict()
for line in inFileLines:
    tempLineList = list(line.split())
    for word in tempLineList:
        if word not in words:
            words[word] = 0
        words[word] += 1
s = []
for word in words:
    s.append([-words[word], word])
s.sort()
print(s[0][1])
