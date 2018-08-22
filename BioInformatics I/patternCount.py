with open('./data/dataset_2_7.txt') as dataFile:
    fullString = dataFile.readline().rstrip()
    testElement = dataFile.readline().rstrip()

x = 0

for i in range(0, len(fullString)-len(testElement)+1) :
    if fullString[i: i+len(testElement)] == testElement: x += 1

print(x)



