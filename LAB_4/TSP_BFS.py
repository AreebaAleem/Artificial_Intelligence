
class Node:
    def __init__(self, name, actions=None, parent=None):
        self.name = name
        self.actions = actions if actions else []
        self.parent = parent

def BFS():
    initialState = 'Arad'
    goalState = 'Bucharest'

    graph = {
    'Arad': Node('Arad',['Sibiu', 'Zerind', 'Timisoara']),
    'Zerind': Node('Zerind',['Arad', 'Oradea']),
    'Oradea': Node('Oradea',['Zerind', 'Sibiu']),
    'Sibiu': Node('Sibiu',['Arad', 'Oradea', 'Fagaras', 'Rimnicu']),
    'Timisoara': Node('Timisoara',['Arad', 'Lugoj']),
    'Lugoj': Node('Lugoj',['Timisoara', 'Mehadia']),
    'Mehadia': Node('Mehadia',['Lugoj', 'Drobeta']),
    'Drobeta': Node('Drobeta',['Mehadia', 'Craiova']),
    'Craiova': Node('Craiova',['Drobeta', 'Rimnicu', 'Pitesti']),
    'Rimnicu': Node('Rimnicu',['Sibiu', 'Craiova', 'Pitesti']),
    'Fagaras': Node('Fagaras',['Sibiu', 'Bucharest']),
    'Pitesti': Node('Pitesti',['Rimnicu', 'Craiova', 'Bucharest']),
    'Bucharest': Node('Bucharest',['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni']),
    'Giurgiu': Node('Giurgiu',['Bucharest']),
    'Urziceni': Node('Urziceni',['Bucharest', 'Vaslui', 'Hirsova']),
    'Hirsova': Node('Hirsova',['Urziceni', 'Eforie']),
    'Eforie': Node('Eforie',['Hirsova']),
    'Vaslui': Node( 'Vaslui',['Iasi', 'Urziceni']),
    'Iasi': Node('Iasi',['Vaslui', 'Neamt']),
    'Neamt': Node('Neamt',['Iasi'])
}

    frontier = [initialState]
    explored = []

    while frontier:
        currentNode = frontier.pop(0)
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

solution = BFS()
print(solution)

