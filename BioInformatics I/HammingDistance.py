def HammingDistance(stringA, stringB):
    distance = 0
    for index, letter in enumerate(stringA):
        if stringB[index] != letter or index >= len(stringB):
            distance += 1

    if(len(stringB) > len(stringA)):
        distance += len(stringB) - len(stringA)
    return distance

with open('../../data/dataset_9_3.txt') as inputFile:
    compareFirst = inputFile.readline().rstrip()
    compareSecond = inputFile.readline().rstrip()
    
print(HammingDistance(compareFirst, compareSecond))
