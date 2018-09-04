import HammingDistance as hd
import ApproximatePatternMatch as apm
import FrequentWordsWithMismatches as fw

def MotifEnumeration(dna, k, d):
    patterns = set()
    for i in range (0, len(dna[0])-k+1):
        kmerNeighbors = fw.Neighbors(dna[0][i:i+k], d)
        if kmerNeighbors is not list:
            kmerNeighbors = [kmerNeighbors]
        for kmerNeighbor in kmerNeighbors:
            approved = True
            for j in range(1, len(dna)):
                strand = dna[j]
                if len(apm.ApproximatePatternMatch(kmerNeighbor,strand, d )) == 0:
                    approved = False
                    break
            if approved:
                patterns.add(kmerNeighbor)
    return patterns

dna = []
with open('../../data/dataset_test.txt') as inputFile:
    [kString, dString] = inputFile.readline().split()
    k = int(kString)
    d = int(dString)
    for line in inputFile:
        dna.append(line.rstrip())

print(MotifEnumeration(dna, k, d))