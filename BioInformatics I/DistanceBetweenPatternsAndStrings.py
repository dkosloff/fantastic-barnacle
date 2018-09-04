import HammingDistance as hd

def FindDistance(pattern, dna):
    k = len(pattern)
    distance = 0
    for strand in dna:
        hamDistance = None
        for i in range(0, len(strand)+k+1):
            kmer = strand[i:i+k]
            kmerDistance = hd.Calculate(kmer, pattern)
            if(hamDistance is None or kmerDistance < hamDistance):
                hamDistance = kmerDistance
        distance += hamDistance
    return distance

dna = []
with open( '../../data/dataset_5164_1.txt') as inputFile:
    pattern = inputFile.readline().rstrip()
    for strand in inputFile.readline().rstrip().split():
        dna.append(strand)

print(FindDistance(pattern, dna))