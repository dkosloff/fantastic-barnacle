import sys
import random

class Sequencer:

    def __init__(self):
        pass

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

    def GetDeBruijnGraph(self, k, snippet):
        '''Returns an adjacency list for a deBruijn Graph
        
        Arguments:
            k {int} -- The length of substrings from snippet
            which will be returned
            snippet {str} -- A string for which all the k-length
            substrings and their adjacent substrings will be returned
        
        Returns:
            {str:[str]} -- A dictionary showing all the substrings of
            snippet and their adjacent substrings
        '''

        nodeList = {}
        for i in range(0, len(snippet)-k+1):
            # Get the node and it's connecting node and place them
            # in the dictionary, adding to the list if the first
            # node already exists
            node = snippet[i:i+k-1]
            adjacentNode = snippet[i+1:i+k]
            
            if node not in nodeList:
                nodeList[node] = []
            
            nodeList[node].append(adjacentNode)

        return nodeList

    def GetDeBruijnGraphFromList(self, snippetList):
        '''Returns a deBruijn adjacency list from a list of 
        strings
        
        Arguments:
            snippetList {[str]} -- A list of strings for which to 
            return an adjacency list
        
        Returns:
            {{str:[str]} -- A dictionary showing all the strings of
            snippetList and the related strings in snippetList which match
            all but the last character
        '''

        result = {}
        # Fill the result list with all the prefixes of the snippets
        for snippet in snippetList:
            if snippet not in result:
                result[snippet[0:-1]] = []

        for snippet in snippetList:
            prefix = snippet[0:len(snippet)-1]
            if prefix in result:
                result[prefix].append(snippet[1:len(snippet)])

        return result

    def GetEulerianCycle(self, adjacencyList):

        # The list of nodes visited
        currentPath = []

        traveledEdges = {node : [] for node in adjacencyList.keys()}
        
        untraveledNodes = [*adjacencyList]

        def CreateCycle(startNode):
            # Current path only has the start node, remove it from available
            #  starts and use as the last visited node
            currentPath.clear()
            currentPath.append( startNode )
            untraveledNodes.remove(startNode)
            lastVisited = currentPath[0]

            #  figure out the while...while there is a path from the 
            # lastVisited node which hasn't been travelled before
            while bool(set(adjacencyList[lastVisited]) - set(traveledEdges[lastVisited])):
                print( "available: ", untraveledNodes)
                print(lastVisited)
                
                # The important bit: choose a node from the adjacencyList which hasn't been chosen previously
                nextNode = random.choice( list(set(adjacencyList[lastVisited]) - set(traveledEdges[lastVisited])) )

                traveledEdges[lastVisited].append(nextNode)
                untraveledNodes.remove(nextNode)
                currentPath.append(nextNode)
                lastVisited = nextNode

        # Get a cycle
        CreateCycle( random.choice(list(adjacencyList.keys())) )

        while untraveledNodes : 
            # Get a random node which wasn't visited and which we haven't yet started from 
            newStartingNode = random.choice(untraveledNodes)
            untraveledNodes = [*adjacencyList]
            CreateCycle( newStartingNode )
        
        # Return the path if all edges have been traveled
        return currentPath