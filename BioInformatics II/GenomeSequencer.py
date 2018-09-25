import math

class Sequencer:

    def __init__(self):
        pass
        # Any initialization, class data members you need
        # would be put here
    
    #  There are no private members or methods

    def StringComposition(self, k, inputString):
        '''Returns all the substrings of length 'k' which exist in 
        inputString
        
        Arguments:
            k {int} -- The length of the substrings in inputString
            which will be returned
            inputString {str} -- The string for which to return the 
            k-length substrings that compose it
        
        Returns:
            [str] -- A list of substrings of k-length which are in 
            inputString
        '''
        composition = []

        for i in range(0, len(inputString)-k+1):
            composition.append(inputString[i:i+k])
        return composition

    def StringReconstruction(self, snippetList):
        '''Takes a list of overlapping DNA snippets and 
        reconstructs the string that they represent
        
        Arguments:
            snippetList {[str]} -- A list of strings which overlap each other
            by all but one character
        
        Returns:
            str -- The reconstructed string
        '''
        # Get all but the last character from the first snippet
        result = snippetList[0][0:len(snippetList[0])-1]

        # Each snippet adds one more character to the result
        for snippet in snippetList:
            result += snippet[len(snippet)-1]
        return result

    def GetAdjacencyList(self, snippetList):
        '''Returns an adjacency list as a dictionary 
        for all strings in the snippetList which share all
        but the last character
        
        Arguments:
            snippetList {[str]} -- The list of strings for which an
            adjacency list will be returned
        
        Returns:
            {str:[str]} -- A dictionary containing each of the items
            in the snippetList and their adjacent items
        '''
        result = {}
        for snippet in snippetList:
            if snippet not in result:
                result[snippet] = []

        for snippet in snippetList:
            for item in result:
                if item[1:] == snippet[0:-1]:
                    result[item].append(snippet)

        return result