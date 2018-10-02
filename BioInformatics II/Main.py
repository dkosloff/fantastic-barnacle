import GenomeSequencer as gs
'''The entry point for the GenomeSequencer Program
'''
inputData = {}
with open('data/dataset_test.txt') as inputFile:
    for line in inputFile:
        splitLine = line.strip().replace(' ', '').split('->')
        inputData[ splitLine[0] ] = splitLine[1].split(',')

result = gs.Sequencer().GetEulerianCycle(inputData)

for item in result:
    print(item, sep="->")