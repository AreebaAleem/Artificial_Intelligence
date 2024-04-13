import math

class Node:
    def __init__(self, state, parent, actions, totalCost, heuristic):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost
        self.heuristic = heuristic

def Astar():
    initialState = 'A'
    goalState = 'Y'


    graph = {
        'A': Node('A', None, [('F', 1)], (0, 0), 0),
        'B': Node('B', None, [('C', 1), ('G', 1)], (0, 2), 0),
        'C': Node('C', None, [('B', 1), ('D', 1)], (0, 3), 0),
        'D': Node('D', None, [('C', 1), ('E', 1)], (0, 4), 0),
        'E': Node('E', None, [('D', 1)], (0, 5), 0),
        'F': Node('F', None, [('A', 1), ('H', 1)], (1, 0), 0),
        'G': Node('G', None, [('B', 1), ('J', 1)], (1, 2), 0),
        'H': Node('H', None, [('F', 1), ('I', 1), ('M', 1)], (2, 0), 0),
        'I': Node('I', None, [('N', 1), ('J', 1)], (2, 1), 0),
        'J': Node('J', None, [('G', 1), ('I', 1)], (2, 2), 0),
        'K': Node('K', None, [('L', 1), ('P', 1)], (2, 4), 0),
        'L': Node('L', None, [('K', 1), ('Q', 1)], (2, 5), 0),
        'M': Node('M', None, [('H', 1), ('N', 1), ('R', 1)], (3, 0), 0),
        'N': Node('N', None, [('I', 1), ('M', 1), ('S', 1)], (3, 1), 0),
        'O': Node('O', None, [('P', 1), ('U', 1)], (3, 3), 0),
        'P': Node('P', None, [('Q', 1), ('O', 1)], (3, 4), 0),
        'Q': Node('Q', None, [('L', 1), ('P', 1), ('V', 1)], (3, 5), 0),
        'R': Node('R', None, [('M', 1), ('S', 1)], (4, 0), 0),
        'S': Node('S', None, [('N', 1), ('R', 1), ('T', 1)], (4, 1), 0),
        'T': Node('T', None, [('S', 1), ('U', 1), ('W', 1)], (4, 2), 0),
        'U': Node('U', None, [('O', 1), ('T', 1)], (4, 3), 0),
        'V': Node('V', None, [('Q', 1), ('Y', 1)], (4, 5), 0),
        'W': Node('W', None, [('T', 1)], (5, 2), 0),
        'X': Node('X', None, [('Y', 1)], (5, 4), 0),
        'Y': Node('Y', None, [('V', 1), ('X', 1)], (5, 5), 0),
    }


    frontier = [(initialState, 0)]
    explored = {}

    while frontier:
        currentNode = frontier[0][0]
        currentCost = frontier[0][1]
        del frontier[0]

        if currentNode == goalState:
            return actionSequence(graph, initialState, goalState)

        if currentNode in explored and explored[currentNode] <= currentCost:
            continue

        explored[currentNode] = currentCost

        for child in graph[currentNode].actions:
            childNode = child[0]
            actionCost = child[1]
            newCost = currentCost + actionCost

            if childNode not in explored or newCost < explored[childNode]:
                heuristicCost = math.sqrt((graph[goalState].heuristic[0] - graph[childNode].heuristic[0]) ** 2 +
                                          (graph[goalState].heuristic[1] - graph[childNode].heuristic[1]) ** 2)
                frontier.append((childNode, newCost + heuristicCost))
                graph[childNode].totalCost = newCost
                graph[childNode].parent = currentNode

    return None

def actionSequence(graph, initialState, goalState):
    solution = [goalState]
    currentParent = graph[goalState].parent
    while currentParent is not None:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution

solution = Astar()
print(solution)