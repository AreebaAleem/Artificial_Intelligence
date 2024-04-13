import math

class Node:
    def __init__(self, state, parent, actions, totalCost, heuristic):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost
        self.heuristic = heuristic

def Astar():
    initialState = 'Arad'
    goalState = 'Bucharest'

    graph = {
        'Arad': Node('Arad', None, [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)], 0, 366),
        'Zerind': Node('Zerind', None, [('Arad', 75), ('Oradea', 71)], 0, 374),
        'Oradea': Node('Oradea', None, [('Zerind', 71), ('Sibiu', 151)], 0, 380),
        'Sibiu': Node('Sibiu', None, [('Arad', 140), ('Oradea', 151), ('Fagaras', 100), ('Rimnicu Vilcea', 80)], 0, 253),
        'Fagaras': Node('Fagaras', None, [('Bucharest', 211), ('Sibiu', 100)], 0, 178),
        'Rimnicu Vilcea': Node('Rimnicu Vilcea', None, [('Sibiu', 80), ('Pitesti', 97), ('Craiova', 146)], 0, 193),
        'Pitesti': Node('Pitesti', None, [('Rimnicu Vilcea', 97), ('Bucharest', 101), ('Craiova', 138)], 0, 100),
        'Craiova': Node('Craiova', None, [('Dobreta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)], 0, 160),
        'Dobreta': Node('Dobreta', None, [('Mehadia', 75), ('Craiova', 120)], 0, 242),
        'Mehadia': Node('Mehadia', None, [('Dobreta', 75), ('Lugoj', 70)], 0, 241),
        'Lugoj': Node('Lugoj', None, [('Mehadia', 70), ('Timisoara', 111)], 0, 244),
        'Timisoara': Node('Timisoara', None, [('Arad', 118), ('Lugoj', 111)], 0, 329),
        'Bucharest': Node('Bucharest', None, [], 0, 0),
    }

    def findMin(frontier):
        minV = math.inf
        node = ''
        for f in frontier:
            if f[1] < minV:
                minV = f[1]
                node = f[0]
        return node

    frontier = [(initialState, 0, graph[initialState].heuristic)]
    explored = {}

    while frontier:
        currentNode = findMin(frontier)

        if currentNode == goalState:
            return actionSequence(graph, initialState, currentNode)

        frontier = [(node, totalDist, heuristic) for node, totalDist, heuristic in frontier if node != currentNode]
        explored[currentNode] = graph[currentNode].totalCost

        for child in graph[currentNode].actions:
            childNode = child[0]
            actionCost = child[1]
            newCost = graph[currentNode].totalCost + actionCost

            if childNode in explored:
                if newCost >= explored[childNode]:
                    continue

            if not any(childNode == node for node, _, _ in frontier):
                heuristicCost = graph[childNode].heuristic
                totalCost = newCost + heuristicCost
                frontier.append((childNode, totalCost, heuristicCost))
                graph[childNode].totalCost = newCost
                graph[childNode].parent = currentNode

def actionSequence(graph, initialState, goalState):
    solution = [(goalState, graph[goalState].totalCost + graph[goalState].heuristic)]
    currentParent = graph[goalState].parent
    while currentParent is not None:
        solution.append((currentParent, graph[currentParent].totalCost + graph[currentParent].heuristic))
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution

solution = Astar()
print(solution)