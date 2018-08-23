import HammingDistance

nucleotides = ['A', 'C', 'G', 'T']

def MostFrequentWithMismatches( test, k, d):
    '''Outputs a file with the most frequent words of k-length 
    that almost match the text (the matches can be off by d characters)

    Arguments:
        test {str} -- The string to be searched
        k {int} -- The length of the words to search for
        d {int} -- The number of characters that can be wrong and
        still consider the word a match
    '''


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
    if d == 0:
        return pattern

    if len(pattern) == 1:
        return nucleotides
    
    neighborhood = []
    suffix = pattern[1:]
    suffixNeighbors = Neighbors(suffix, d)

    for n in suffixNeighbors:
        if HammingDistance.Calculate(suffix, n) < d:
            for nuc in nucleotides:
                neighborhood.append(nuc + n)
        else:
            neighborhood.append(pattern[0] + n)

    return neighborhood

with open('./../../data/dataset_3014_4.txt') as inputFile:
    pattern = inputFile.readline().rstrip()
    variance = int(inputFile.readline().rstrip())

results = Neighbors(pattern, variance)

with open('./../../results/mismatchResults.txt', 'w') as outFile:
    for result in results:
        print(result, file=outFile)