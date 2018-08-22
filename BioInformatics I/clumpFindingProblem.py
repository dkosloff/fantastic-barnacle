## This Solution works, but only because all the crazy +1 index
## corrections.  It definitely could use some more thought.


# addToDict(): each time you add one, check to see if it's
# above the minOccurrences amount and if it is, add it to the results

occurrenceDict = {}
results = list()

def addToDict(kmer, minOccurrences):
    if(kmer not in occurrenceDict):
        occurrenceDict[kmer] = 0

    occurrenceDict[kmer] += 1

    if(occurrenceDict[kmer] >= minOccurrences and results.count(kmer) == 0):
        results.insert(len(results), kmer)


#removeFromDict() : decrease the amount in the dictionary
def removeFromDict(kmer):
    occurrenceDict[kmer] = occurrenceDict[kmer] - 1

def ClumpFinding(genome, k, L, t):

    # start from 0 to kmerLength
    # find all the different kmers in the genome for
    # the initial window and add them to the dictionary using addToDict()
    for i in range(0, L-k+1):
        addToDict(genome[i:k+i], t)

    # Slide the window along, removing the previous result which is no
    # longer in the genomeWindow, and adding the new kmer which is revealed
    # by the new window , ie [acgtt] -> a[cgtta] would remove 'ac' for a
    # 2-mer and add 'ta'

    # A Note:  I do not like this extra '+1' at the end.  Not sure why it 
    # has to be there
    for i in range(0, len(genome)-L + 1 ):
        removeFromDict(genome[i:k+i])
        addToDict(genome[L-k+i+1:L+i+1], t)
    return results

        # Optionally print the results to a file...
    # with open('results/clumpResults.txt', 'w') as outputFile:
    #     for result in results:
    #         print(result, end=" ", file=outputFile)

with open('data/E_Coli.txt') as genomeFile:
    genome = genomeFile.readline().rstrip().upper()
    # these were used with dataset_4_5.txt
    # variables = genomeFile.read().rstrip()
    # [kmerLength, genomeWindow, minOccurrences] = list(
    #     map(int, variables.split()))
    genome = 'CCACGCGGTGTACGCTGCAAAAAGCCTTGCTGAATCAAATAAGGTTCCAGCACATCCTCAATGGTTTCACGTTCTTCGCCAATGGCTGCCGCCAGGTTATCCAGACCTACAGGTCCACCAAAGAACTTATCGATTACCGCCAGCAACAATTTGCGGTCCATATAATCGAAACCTTCAGCATCGACATTCAACATATCCAGCG'
    kmerLength = 3
    genomeWindow = 25
    minOccurrences = 3

    print( ClumpFinding(genome, kmerLength, genomeWindow, minOccurrences) )