import HammingDistance as hd
import ComputingFrequencies as cf
import reverseComplement as reverse
nucleotides = ['A', 'C', 'G', 'T']

def MostFrequentWithMismatches( text, k, d):
    '''Outputs a file with the most frequent words of k-length 
    that almost match the text (the matches can be off by d characters)

    Arguments:
        text {str} -- The string to be searched
        k {int} -- The length of the words to search for
        d {int} -- The number of characters that can be wrong and
        still consider the word a match
    '''
    # Holds indexes for all the possible 'neighbor' patterns
    frequencies = [0] * (4**k)
    highestFrequency = 0
    pattern = ''

    # Go through the text, k characters at a time
    for i in range(0, len(text)-k):
        pattern = text[i:k+i]
        #  Get all the neighbors (optionally include the 
        # reverse complements of the pattern)
        neighborhood = Neighbors(pattern, d) + \
            Neighbors(reverse.Calulate(pattern), d )
        for neighbor in neighborhood:
            index = cf.PatternToNumber(neighbor)
            frequencies[index] += 1
            if frequencies[index] > highestFrequency:
                highestFrequency = frequencies[index]
    
    mostFrequent = []
    for index, value in enumerate(frequencies):
        if value == highestFrequency:
            mostFrequent.append( cf.NumberToPattern(index, k) )
    return mostFrequent



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
        if hd.Calculate(suffix, n) < d:
            for nuc in nucleotides:
                neighborhood.append(nuc + n)
        else:
            neighborhood.append(pattern[0] + n)

    return neighborhood

with open('./../../data/dataset_9_8.txt') as inputFile:
    text = inputFile.readline().rstrip()
    args = inputFile.readline().rstrip()
    [k, d] = list(map(int, args.split()))

results = MostFrequentWithMismatches(text, k, d)

with open('./../../results/FrequentWithMismatchResults.txt', 'w') as outFile:
    for result in results:
        print(result, end=' ', file=outFile)