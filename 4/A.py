with open('input.txt', 'r', encoding='utf8') as f:
    synonyms = dict()
    n = int(f.readline())
    for i in range(n):
        tempWord, tempSynonyms = f.readline().split()
        synonyms[tempWord] = tempSynonyms
        synonyms[tempSynonyms] = tempWord
    print(synonyms[f.readline().strip()])

