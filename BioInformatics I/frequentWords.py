def FrequentWords(Text, KmerLength):
    kmerDict = {}
    maxCount = 0
    results = []

    for i in range(0, len(text) - kmerLength +1):

        word = text[i : i+kmerLength]

        if word in kmerDict:
            kmerDict[word] += 1
        else:
            kmerDict[word] = 1

        if kmerDict[word] > maxCount : maxCount = kmerDict[word]

    for record, count in kmerDict.items():
        if int(count) == maxCount:
            results.append(record)

    results.sort()

    return ' '.join(results)

with open('./data/dataset_2_10.txt') as dataFile:
    text = dataFile.readline().rstrip()
    kmerLength = int(dataFile.readline().rstrip())

    text = 'ACGCGGCTCTGAAA'
    kmerLength = 2
    print(FrequentWords(text, kmerLength))

