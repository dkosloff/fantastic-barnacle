import GenomeSequencer as gs
'''The entry point for the GenomeSequencer Program
'''
inputData = {}
with open('data/dataset_test.txt') as inputFile:
    for line in inputFile:
        splitLine = line.strip().replace(' ', '').split('->')
        inputData[ int(splitLine[0]) ] = list(map(int, splitLine[1].split(',')))

result = gs.Sequencer().GetEulerianCycle(inputData)

# with open('results/dataset_203_2_results.txt', 'w') as output:
print(*result, sep="->")