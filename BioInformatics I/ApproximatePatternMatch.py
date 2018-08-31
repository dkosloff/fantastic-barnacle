import HammingDistance

def ApproximatePatternMatch(pattern, text, allowances):
    matches = []
    patternLength = len(pattern)
    for i in range(0, len(text)-patternLength+1):
        if(i == len(text)-patternLength-1):
            x=3
        if( HammingDistance.Calculate(text[i:patternLength+i], pattern) <= allowances):
            matches.append(i)

    return matches

with open('../../data/dataset_9_4.txt') as inputFile:
    pattern = inputFile.readline().rstrip()
    text = inputFile.readline().rstrip()
    allowances = int(inputFile.readline().rstrip())
    
    with open('../../results/results_9_4.txt', 'w') as resultsFile:
        for result in ApproximatePatternMatch(pattern, text, allowances):
            print( result, end=' ', file=resultsFile)