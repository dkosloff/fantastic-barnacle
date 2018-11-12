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

        # The set of nodes which have unexplored neighbors
        hasUnvisitedNeighbors = set()

        # Get a cycle
        finalCycle = Sequencer.CreateCycle( self, random.choice(list(adjacencyList.keys())), hasUnvisitedNeighbors, adjacencyList)[0]
        tempStack = []
        while len(hasUnvisitedNeighbors) != 0:

            # Get a random node which wasn't visited in this cycle 
            newStartingNode = random.choice( list(hasUnvisitedNeighbors) )

            # Here's where it all comes together. Open up the finalCycle
            # at the newStartingNode, insert a new cycle which starts at
            # that node and then put the top back on the sandwich
            
            # Split the cycle into two sections
            node = finalCycle.pop()
            while node != newStartingNode:
                tempStack.append(node)
                node = finalCycle.pop()

            # A new cycle which intersects this cycle (starts at this node)
            finalCycle += Sequencer.CreateCycle(self, newStartingNode, hasUnvisitedNeighbors, adjacencyList )[0]

            # Put the cycle back together
            while tempStack:
                finalCycle.append(tempStack.pop())
        
        # Return the path if all edges have been traveled
        return finalCycle
    
    def CreateCycle(self, startNode, hasUnvisitedNeighbors, adjacencyList):
        '''Helper function which creates a cycle from an adjacency list
        NOTE: this function modifies adjacencyList and hasUnvisitedNeighbors
        
        Arguments:
            startNode {int} -- A number indicating which node in adjacencyList 
            should be used as the starting node
            hasUnvisitedNeighbors {set} -- A set of nodes which have unexplored
            neighbors -will be updated with new members in this method
            adjacencyList {{int:[int]}} -- A mapping of nodes to their neighbors
            -will be updated in this method, all nodes returned from this method
            will be removed from this list
        
        Returns:
            [([int], int, int)] -- A cycle found in adjacencyList, plus any found
            starting node or ending node (those without connecting nodes)
        '''

        currentCycle = [startNode]
        foundStartNode = None
        foundEndNode = None
        # Stop when we have two of the current node in the 
        # cycle (the cycle is complete at this point)
        while currentCycle[-1] != currentCycle[0] or len(currentCycle) == 1:
            currentNode = currentCycle[-1]

            try:
                nextNode = random.choice( adjacencyList[currentNode] )
                if nextNode not in adjacencyList:
                    foundEndNode = nextNode
                    adjacencyList[currentNode].remove(nextNode)
                    nextNode = random.choice( adjacencyList[currentNode] )

            except:
                print("Trying to access node which doesn't exist!!")

            # Housekeeping, move from neighbor list to currentCycle, keep track of or delete
            adjacencyList[currentNode].remove(nextNode)
            if len(adjacencyList[currentNode]) > 0:
                hasUnvisitedNeighbors.add(currentNode)
            else:
                if currentNode in hasUnvisitedNeighbors:
                    hasUnvisitedNeighbors.remove(currentNode)
                del adjacencyList[currentNode]

            currentCycle.append(nextNode)
            
        return (currentCycle, foundStartNode, foundEndNode)

    def GetEulerianPath(self, adjacencyList):
        # When trying to get a cycle, if you are trying to get 
        # a value of adjacencyList[currentNode] in createCycle above 
        # and it doesn't exist, it's the end node.  The node that is 
        # left over when 
        startNode = None
        endNode = None

        # We can now send back the end node, but we need to find the start node.
        # It has to do with 

