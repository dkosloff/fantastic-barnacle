import ProfileMostProbableKmer as pMostProb

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

    def getProfile(dnaRow, j, k):
        '''Creates a profile (a probability matrix) of size[dnaSnippet-k+1][k] 
        from the given string dnaSnippet 
        
        Arguments:
            row {int} -- The row in dna to use as a the source
            j {int} -- The starting index of the dna strings 
            k {int} -- The length of the string to create a profile for
        
        Returns:
            {char:[float]} -- A dict of floating points denoting the
            probability of the character (dict key) existing in that 
            position in the string (e.g. {'A' : [0.25, ...] shows that 'A'
            should occur in the first position in a string 1/4 of the time)
        '''
        counts = {'A':[], 'C':[], 'T':[], 'G':[]}
        
        for countList in counts.values():
            for i in range(0,k):
                countList.append(0)

### This may be the problem...we should be returning just the probability 
# for the first kmer in row one when dnaRow = 1, then when dnaRow = 2, we 
# should be calculating it based on row 1 AND 2, so with each row, the amount
# of values going into the calculation increases by k (not sure if this is happening)
###

# Seems to be working okay, but it's not getting the answer 
# 'CAG', 'CAG', 'CAA', 'CAA', 'CAA' SO MAYBE THE findKmer method is messsed up

        # Fill in the counts. We are counting from the first row
        # to just before dnaRow
        for row in range(0, dnaRow):
            for col in range(j, j+k):
                counts[ dna[row][col] ][col-j] += 1
        
        #  Transform the count list into a probability matrix
        for letter in counts:
            for idx in range(0, len(counts[letter])):
                counts[letter][idx] /= dnaRow

        return counts

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
            profile = getProfile(dnaRow, j, k)
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
        print(str(motifs) + ": " + str(score))
    return score

dna = []
with open('data/dataset_test.txt') as inputFile:
    [k,t] = map(int, inputFile.readline().split())
    for line in inputFile:
        dna.append(line.rstrip())

print(Search(dna,k,t))
