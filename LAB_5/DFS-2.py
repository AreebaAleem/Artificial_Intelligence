class Node:
    def __init__(self, name, actions=None, parent=None):
        self.name = name
        self.actions = actions if actions else []
        self.parent = parent

def DFS():
    initialState = 'A'
    goalState = 'F'

    graph = {
        'A': Node('A', ['B', 'C', 'E']),
        'B': Node('B', ['A', 'D', 'E']),
        'C': Node('C', ['A', 'F', 'G']),
        'D': Node('D', ['B', 'E']),
        'E': Node('E', ['A', 'B', 'D']),
        'F': Node('F', ['C']),
        'G': Node('G', ['C'])
    }

    frontier = [initialState]
    explored = []

    while frontier:
        currentNode = frontier.pop()
        explored.append(currentNode)
        for child in graph[currentNode].actions:
            if child not in frontier and child not in explored:
                graph[child].parent = currentNode
                if child == goalState:
                    return actionSequence(graph, initialState, goalState)
                frontier.append(child)

def actionSequence(graph, initialState, goalState):
    solution = [goalState]
    currentParent = graph[goalState].parent
    while currentParent:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution

solution = DFS()
print(solution)