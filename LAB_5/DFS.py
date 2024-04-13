class Node:
    def __init__(self, name, actions=None, parent=None):
        self.name = name
        self.actions = actions if actions else []
        self.parent = parent

def DFS():
    initialState = 's'
    goalState = 'g'

    graph = {
        's': Node('s', ['d', 'e', 'p']),
        'a': Node('a'),
        'b': Node('b', ['a']),
        'c': Node('c', ['a']),
        'd': Node('d', ['b', 'c', 'e']),
        'e': Node('e', ['h', 'r']),
        'f': Node('f', ['c', 'g']),
        'g': Node('g'),
        'h': Node('h', ['p', 'q']),
        'p': Node('p', ['q']),
        'q': Node('q'),
        'r': Node('r', ['f']),
    }

    frontier = [initialState]
    explored = []

    def actionSequence(graph, initialState, goalState):
        solution = [goalState]
        currentParent = graph[goalState].parent
        while currentParent:
            solution.append(currentParent)
            currentParent = graph[currentParent].parent
        solution.reverse()
        return solution

    while frontier:
        currentNode = frontier.pop()
        explored.append(currentNode)
        for child in graph[currentNode].actions:
            if child not in frontier and child not in explored:
                graph[child].parent = currentNode
                if child == goalState:
                    return actionSequence(graph, initialState, goalState)
                frontier.append(child)

solution = DFS()
print(solution)
