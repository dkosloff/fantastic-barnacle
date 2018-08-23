def HammingDistance(stringA, stringB):
    '''Finds the number of characters that vary
    between two strings
    
    Arguments:
        stringA {string} -- The first string to compare
        stringB {string} -- The second string to compare
    
    Returns:
        integer -- The number of characters that are different
    '''

    distance = 0
    for index, letter in enumerate(stringA):
        if stringB[index] != letter or index >= len(stringB):
            distance += 1

    if(len(stringB) > len(stringA)):
        distance += len(stringB) - len(stringA)
    return distance

# with open('../../data/dataset_9_3.txt') as inputFile:
#     compareFirst = inputFile.readline().rstrip()
#     compareSecond = inputFile.readline().rstrip()
    
# print(HammingDistance(compareFirst, compareSecond))
