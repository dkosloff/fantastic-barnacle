## What this does is make a list of all possible k-mers,
## then adds a number associated with the count of each k-mer
## as it scans the Text


letters = ['A', 'C', 'G', 'T']

def PatternToNumber(Pattern):
    base = len(letters)
    sum = 0
    for i in range (0, len(Pattern)):
        sum += (base**(len(Pattern)-i-1)) * letters.index(Pattern[i])
    return sum


def PatternToNumberRecursive(Pattern):
    base = len(letters)
    if ((len(Pattern) == 0)):
        return 0
    return base*PatternToNumber(Pattern[0:-1])+letters.index(Pattern[-1])


def NumberToPattern(index, k):
    pattern = ''
    base = len(letters)

    for i in range( k-1, -1, -1):
        letterIndex = int(index / base**i)
        pattern += letters[letterIndex]
        index -= (base**i * letterIndex)

    return pattern

def ComputingFrequencies(Text, k):
    # initalize the properly-sized array with all zeroes
    largestIndexPattern = ''
    for y in range(0, k):
        largestIndexPattern += letters[len(letters)-1]
    results = [0] * (PatternToNumber( largestIndexPattern )+1)
    
    for i in range(0, len(Text)-k+1):
        results[ PatternToNumber(Text[i:k+i]) ] += 1

    return results


# with open('data\dataset_2994_5.txt') as inputFile:
#     var1 = inputFile.readline().rstrip()
#     var2 = int(inputFile.readline().strip())

# with open('results/test2994_5results.txt', 'w') as output:
#     resultSet = ComputingFrequencies(var1, var2)
#     for result in resultSet:
#         print( result, end=' ', file=output)