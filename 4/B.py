inFile = open('input.txt', 'r', encoding='utf8')
inFileLines = inFile.readlines()
words = dict()
for line in inFileLines:
    tempLineList = list(line.split())
    for word in tempLineList:
        if word not in words:
            words[word] = 0
        print(words[word], end=' ')
        words[word] += 1
