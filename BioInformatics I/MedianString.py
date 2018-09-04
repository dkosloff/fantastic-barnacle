import ComputingFrequencies as cf 
import HammingDistance as hd 

def FindMedianString(dna, k):
    
    pattern = None
    bestDistance = None
    bestPattern = None
    finalPattern = ''
    strandDistance = None
    smallestStrandDistance = None

    # Calculate the final pattern in the sequence, i.e. 'T'*k
    for y in range(0, k):
        finalPattern += cf.letters[len(cf.letters)-1]
    lastIndex = cf.PatternToNumber(finalPattern)

    # For all the possible patterns of length k
    for i in range(0, lastIndex + 1):
        
        pattern = cf.NumberToPattern(i,k)
        totalDistance = 0

        # For the given dna strands, go through each one
        # and calculate the hamming distance.  Adding that 
        # distance to the totalDistance
        for strand in dna:
            smallestStrandDistance = None
            for j in range(0, len(strand)-k+1):
                strandDistance = hd.Calculate(strand[j:j+k], pattern)
                if ((smallestStrandDistance == None) or 
                    (strandDistance < smallestStrandDistance)):
                    smallestStrandDistance = strandDistance
            totalDistance += smallestStrandDistance
        if (bestDistance == None) or (totalDistance < bestDistance) :
            bestDistance = totalDistance
            bestPattern = pattern
    
    return bestPattern

dna = []
with open('../../data/dataset_158_9.txt') as inFile:
    kValue = int(inFile.readline().rstrip())
    for line in inFile:
        dna.append(line)

print( FindMedianString(dna, kValue))