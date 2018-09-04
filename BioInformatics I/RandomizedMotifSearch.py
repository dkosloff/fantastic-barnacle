import GreedyMotifSearch as gms
import ProfileMostProbableKmer as pMostProb
import random
def Search(dna, k, t):

    currentMotif = []
    # For each strand in dna, choose a random starting
    # position for a substring 'k' characters long
    for snippet in dna:
        position = int(random.random()*(len(snippet)-k-1))
        currentMotif.append(snippet[position:position+k])

    bestMotif = currentMotif
    bestScore = gms.Score(currentMotif)
    while True:
        # Get the profile from this random collection, use that to 
        # find the kmers which would fit it.  Score those new kmers
        # against the old collection.  If the score is worse, just 
        # return the previous, better score.
        profile = gms.getProfile(currentMotif)
        currentMotif = []
        for snippet in dna:
            currentMotif.append(
                pMostProb.FindKmer( snippet, k, profile))
            currentScore = gms.Score(currentMotif)
        if  currentScore < bestScore:
            bestMotif = currentMotif
            bestScore = currentScore 
        else:
            return (bestMotif, bestScore)

dna = []
with open('../../data/dataset_test.txt') as inputFile:
    [k,t] = map(int, inputFile.readline().split())
    for line in inputFile:
        dna.append(line.rstrip())

finalMotif = finalScore = None

(finalMotif, finalScore) = Search(dna, k, t)
for i in range (0, 999):
    result = Search(dna,k,t)
    if result[1] < finalScore:
        finalMotif = result[0]
        finalScore = result[1]

for kmer in finalMotif:
    print(kmer)