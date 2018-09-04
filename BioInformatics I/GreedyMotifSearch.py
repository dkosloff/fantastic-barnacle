import ProfileMostProbableKmer as pMostProb


def getProfile(matrix):
    '''Returns a probability matrix for a given matrix
    by counting the total of each nucleotide in each 
    columns and dividing that count by the total number
    
    Arguments:
        matrix {[[str]]} -- A two-dimensional array 
        of nucleotide characters
    
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


def Search(dna, k, t):
    '''Finds the most likely matching strings of length k
    by comparing all strings of that length in dna, returning
    the collection with the best score 
    
    Arguments:
        dna {[str]]} -- A list of strings which represent 
        the same section from different dna sources
        k {int} -- The number of nucleotides to find (i.e.
        the returned list will have t strings of length k)
        t {int} -- The number of strings in dna
    
    Returns:
        [str] -- A list of t strings of length k which 
        represent the closest matching strings this 
        algorithm could find between all k-length strings in dna
    '''



    # Initialized with the first k characters from each dna string
    bestMotifs = []
    for i in range(0, len(dna)):
        bestMotifs.append(dna[i][0:k])

    # Go thorugh all the substrings of length k in the first dna string
    for j in range(0, len(dna[0])-k+1):
        motifs = []
        motifs.append(dna[0][j:j+k])

        # For the rest of the strings in dna
        for dnaRow in range(1, t):
            # Get a char profile from the current kmer to the 
            # kmer in the last string of dna
            # profile = getProfile(dnaRow, j, k)
            profile = getProfile(motifs)
            motifs.append(pMostProb.FindKmer( dna[dnaRow], k, profile))
        if Score(motifs) < Score(bestMotifs):
            bestMotifs = motifs
    return bestMotifs

def Score(motifs):
    score = 0

    for col in range(0, len(motifs[0])):
        colCount = {'A':0, 'C':0, 'T':0, 'G':0}
        for row in range(0, len(motifs)):
            colCount[motifs[row][col]] += 1
        
        maxValue=0
        for value in colCount.values():
            if value > maxValue:
                maxValue = value
        score += len(motifs)- maxValue
    return score

# dna = []
# with open('../../data/dataset_160_9.txt') as inputFile:
#     [k,t] = map(int, inputFile.readline().split())
#     for line in inputFile:
#         dna.append(line.rstrip())

# for value in Search(dna,k,t):
#     print(value)
