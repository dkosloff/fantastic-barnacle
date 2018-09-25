import GenomeSequencer as gs
'''The entry point for the GenomeSequencer Program
'''

s = []
with open('data/dataset_198_10.txt') as inputFile:
    for line in inputFile:
        s.append(line.rstrip())


result = gs.Sequencer().GetAdjacencyList(s)

with open('results/dataset_198_10_results.txt', 'w') as out:
    for item in result:
        if(len(result[item]) > 0):
            print(item + ' -> ', end='', file=out)
            print(','.join(result[item]), file=out)