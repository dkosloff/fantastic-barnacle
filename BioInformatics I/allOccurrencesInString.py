
def PatternMatching(Pattern, Genome):
    occurrences = []
    result = ''
    for i in range( 0, len(Genome)):
        if(Genome[i:i+len(Pattern)] == Pattern):
            occurrences.append(i)
   
    return ' '.join(map(str, occurrences))

with open('data/dataset_3_5.txt') as stringFile:
    Pattern = stringFile.readline().rstrip().lower()
    Genome = stringFile.readline().rstrip().lower()

    print( PatternMatching(Pattern, Genome))
