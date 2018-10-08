import GenomeSequencer as gs
'''The entry point for the GenomeSequencer Program
'''
inputData = {}
with open('data/dataset_test.txt') as inputFile:
    for line in inputFile:
        splitLine = line.strip().replace(' ', '').split('->')
        inputData[ int(splitLine[0]) ] = list(map(int, splitLine[1].split(',')))

result = gs.Sequencer().GetEulerianCycle(inputData)

# for item in result:
print(*result, sep="->")