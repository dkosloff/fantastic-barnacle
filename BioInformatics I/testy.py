# Write your MotifEnumeration() function here along with any subroutines you need.
# This function should return a list of strings.
def MotifEnumeration(dna, k, d):
    patterns = []
    for i in range (0, len(dna[0])-k+1):
        knobs = Neighbors(dna[0][i:i+k], d)
        for kmerNeighbor in knobs:
            approved = True
            for j in range(1, len(dna)):
                strand = dna[j]
                if len(ApproximatePatternMatch(kmerNeighbor,strand, d )) == 0:
                    approved = False
                    break
            if approved and kmerNeighbor not in patterns:
                patterns.append(kmerNeighbor)
    return patterns

def Neighbors(pattern, d):
    '''Returns all the neighboring nucleotide combinations for a
    given pattern and prefix count (?)
    
    Arguments:
        pattern {str} -- The pattern to return neighbors for
        d {int} -- The number of characters which can be changed
        and be considered a 'neighbor'
    
    Returns:
        neighbors -- A list of neighbors for a pattern
    '''
    nucleotides = ['A', 'C', 'G', 'T']

    if d == 0:
        return [pattern]

    if len(pattern) == 1:
        return nucleotides
    
    neighborhood = []
    suffix = pattern[1:]
    suffixNeighbors = Neighbors(suffix, d)

    for n in suffixNeighbors:
        if HDCalculate(suffix, n) < d:
            for nuc in nucleotides:
                neighborhood.append(nuc + n)
        else:
            neighborhood.append(pattern[0] + n)

    return neighborhood

def ApproximatePatternMatch(pattern, text, allowances):
    matches = []
    patternLength = len(pattern)
    for i in range(0, len(text)-patternLength+1):
        if( HDCalculate(text[i:patternLength+i], pattern) <= allowances):
            matches.append(i)

    return matches

def HDCalculate(stringA, stringB):
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

dna = []
with open('../../data/dataset_test.txt') as inputFile:
    [kString, dString] = inputFile.readline().split()
    k = int(kString)
    d = int(dString)
    for line in inputFile:
        dna.append(line.rstrip())

print(MotifEnumeration(dna, k, d))