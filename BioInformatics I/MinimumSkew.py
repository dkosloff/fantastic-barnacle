def MinimumSkew(strand):
    s = strand[0]
    minSkew = 0 if (s == 'C' or s == 'G') else (-1 if s == 'C' else 1)
    skewLocations = []
    skew = 0
    for index, polymerase in enumerate(strand):
        if( polymerase == 'C' ):
            skew -= 1
        if( polymerase == 'G' ):
            skew += 1
        if (skew < minSkew):
            minSkew = skew
            skewLocations.clear()
            skewLocations.append(index+1)
        elif(skew == minSkew):
            skewLocations.append(index+1)
    return skewLocations

with open('BioInformatics I\data\dataset_7_6.txt') as file:
    strand = file.readline().rstrip()

result = MinimumSkew(strand)

with open('BioInformatics I/results/dataset_7_6_results.txt', 'w') as resultsFile:
    for r in result:
        print(r, end=' ', file=resultsFile)