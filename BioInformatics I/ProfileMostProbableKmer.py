def FindKmer(text, k, profile):
    '''Finds the most likely kmer of all kmers in text, given
    the probability profile.
    
    Arguments:
        text {str} -- The text to search for kmers in 
        k {int} -- The length of candidate strings to search
        for in 'text'
        profile {{string:[float]}} -- A dictionary of the probabilities that 
        each candidate kmer should be computed against. 
    
    Returns:
        {str} -- A kmer found in the text with the highest
        computed probability
    '''
    mostProbable = ''
    highestProbability = -1

    def findProbability(kmer):
        total = 1
        for i in range(0, len(kmer)):
            # Find the letter in index and find the probability
            # in the profile with profile[ltrIdx][i]
            total *= profile[kmer[i]][i]
        return total

    for i in range(0, len(text)-k+1):
        kmer = text[i:i+k]
        probability = findProbability(kmer)
        if probability > highestProbability:
            highestProbability = probability
            mostProbable = kmer
    return mostProbable

profile = []

# with open('data/dataset_159_3.txt') as inputFile:
#     text = inputFile.readline().rstrip()
#     k = int(inputFile.readline().rstrip())
#     for line in inputFile:
#         lineArray = list(map(float, line.split()))
#         profile.append(lineArray)

# print( FindKmer(text, k, profile) )