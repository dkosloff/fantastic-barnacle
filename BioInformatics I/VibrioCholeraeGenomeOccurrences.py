with open('data/Vibrio_cholerae.txt') as stringFile:
    genome = stringFile.readline().rstrip().upper()

item = 'CTTGATCAT'
occurrences = []

for i in range( 0, len(genome)):
    if(genome[i:i+len(item)] == item):
        occurrences.append(i)

with open('results/Vibrio_cholerae_results.txt', 'w') as outputFile:
    for occurrence in occurrences:
        print(occurrence, end=' ', file=outputFile)