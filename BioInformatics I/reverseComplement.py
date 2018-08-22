def ReverseComplement(pattern):
    result = ''

    for i in range(len(pattern)-1, -1, -1):
        if(pattern[i] == 'A'):
            result += 'T'
        elif(pattern[i] == 'T'):
            result += 'A'
        elif(pattern[i] == 'G'):
            result += 'C'
        elif(pattern[i] == 'C'):
            result += 'G'

    return result


with open('data/dataset_3_2.txt') as patternFile:
    pattern = patternFile.readline().rstrip().upper()
    print( ReverseComplement(pattern) )


# with open("results/dataset_3_2.txt", "w") as text_file:
#     print(result, file=text_file)