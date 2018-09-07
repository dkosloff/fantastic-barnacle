import random
import GreedyMotifSearch as gms
import HammingDistance as hd

def GibbsSampler(dna, k, t, n):

    bestMotifs = []
    for snippet in dna:
        idx = int(random.random()*(len(snippet)-k+1))
        bestMotifs.append(snippet[idx:idx+k])
    
    bestScore = gms.Score(bestMotifs)

    for i in range(0, 2000):
        # Select a random string in dna for which 
        # to find a better matching kmer (substring)
        dnaStringIndex = int(random.random()*(t))
        # Returns a probability profile to generate a 'biased' index
        profile = GetProfileExcept(bestMotifs, dnaStringIndex)
        newIndex = RandomFromProfile(profile, k, dna[dnaStringIndex])
        # Use the index to replace the kmer at bestMotifs[dnaStringIndex]
        testMotifs = bestMotifs.copy()
        testMotifs[dnaStringIndex] = dna[dnaStringIndex][newIndex:newIndex+k]
        # Save the new, modified motifs if better
        thisScore = gms.Score(testMotifs)
        if  thisScore <= bestScore:
            bestMotifs = testMotifs
            bestScore = thisScore

    return (bestScore, bestMotifs)


def GetProfileExcept(matrix, exclusionIndex):
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

    counts = {'A':[], 'C':[], 'G':[], 'T':[]}

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
        if row == exclusionIndex:
            continue
        for col in range(0, len(matrix[row])):
            counts[ matrix[row][col] ][col] += 1

    # Transform the count list into a probability matrix
    # Divide by matrix-length-1 + 4 because of the ones 
    # added intially and the one row you're excluding
    for letter in counts:
        for idx in range(0, len(counts[letter])):
            counts[letter][idx] /= (len(matrix) -1 + 4)

    return counts

def RandomFromProfile(probabilityMatrix, k, dnaSnippet):

    # This will hold the probabilities for each possible 
    # kmer in the row
    kmerProbabilitiesInString = []
    for i in range(0, len(dnaSnippet)-k+1):
        
        # Multiply the probabilities of each letter 
        # occurring to get the overall probability of the 
        # string's occurrence
        probability = 1
        for index, letter in enumerate(dnaSnippet[i:i+k]):
            probability *= probabilityMatrix[letter][index]

        kmerProbabilitiesInString.append(probability)


    # Now that we have a probability for each possible 
    # index of a kmer in the dnaSnippet, we can choose one 
    # based on those probabilities

    return GetWeightedDieRoll(kmerProbabilitiesInString)

def GetWeightedDieRoll(weightList):

    sum = 0
    for value in weightList:
        sum += value

    for index, value in enumerate(weightList):
        weightList[index] = value / sum
    
    roll = random.random()

    rollingSum = 0
    for index, value in enumerate(weightList):
        if (rollingSum + value) >= roll:
            return index
        rollingSum += value





dna = []
with open('data/dataset_163_4.txt') as inputFile:
    [k, t, n] = map(int, inputFile.readline().split())
    for line in inputFile:
        dna.append( line.rstrip() )

result = GibbsSampler(dna, k, t, n)
score = result[0]
bestResult = result[1]

for i in range(0, 19):
    result = GibbsSampler(dna, k, t, n)
    if result[0] < score:
        score = result[0]
        bestResult = result[1]

print("LowestScore: " + str(score))

with open('results/dataset_163_4_results.txt', 'w') as output:
    for snippet in bestResult:
        print(snippet, file=output)