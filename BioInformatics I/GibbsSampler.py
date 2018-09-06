import random

def GibbsSampler(dna, k, t, n):

    bestMotifs = []

    for snippet in dna:
        idx = random.random()*(len(snippet)-k)
        bestMotifs.append(snippet[idx:idx+k])
    
    for i in range(0, n):
        # Select a random string in dna for which 
        # to find a better matching kmer (substring)
        dnaString = random.random()*(t-1)
        profile = getProfileExcept(dna, dnaString)

    return bestMotifs


def getProfileExcept(matrix, exclusionIndex):
    '''Returns a probability matrix for a given matrix
    by counting the total of each nucleotide in each 
    column and dividing that count by the total number,
    excluding the exclusionIndex
    
    Arguments:
        matrix {[[str]]} -- A two-dimensional array 
        of nucleotide characters
        exclusionIndex {int} -- The index of a row to 
        exclude from the count
    
    Returns:
        {char:[float]} -- A dictionary containing the 
        probabilities of each letter in each position
    '''

    counts = {'A':[], 'C':[], 'T':[], 'G':[]}

    # Initialize to ones to take advantage of Laplace's
    # rule of succession (the absence of a nucleotide 
    # in a position doesn't mean it should NEVER be 
    # considered as a possible match, i.e. have probability 0)
    for countList in counts.values():
        for i in range(0,len(matrix[0])):
            countList.append(1)

    # Each position in matrix will have a letter
    # update the appropriate index in counts based off
    # that letter and column, counts ends up with the 
    # the total for each letter in each column
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            counts[ matrix[row][col] ][col] += 1

    # Transform the count list into a probability matrix
    # Divide by matrix-length + 4 because of the ones added intially
    for letter in counts:
        for idx in range(0, len(counts[letter])):
            counts[letter][idx] /= (len(matrix) + 4)

    return counts