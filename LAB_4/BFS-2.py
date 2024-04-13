
class Node:
    def __init__(self, name, actions=None, parent=None):
        self.name = name
        self.actions = actions if actions else []
        self.parent = parent

def BFS():
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

# def BFS():
#     initialState='A'
#     goalState='F'

# graph={
#     'A':Node('A',None['B','C','E'],None),
#     'B':Node('B',None['A','D','E'],None),
#     'C':Node('C',None['A','F','G'],None),
#     'D':Node('D',None['B','E'],None),
#     'E':Node('E',None['A','B','D'],None),
#     'F':Node('F',None['C'],None),
#     'G':Node('G',None['C'],None)
# }

# frontier={initialState}
# explored={}

# while len(frontier)!=0:
#     currentNode = frontier.pop(0)
#     explored.append(currentNode)
#     for child in graph[currentNode].actions:
#         if child not in frontier and child not in explored:
#             graph[child].parent = currentNode
#             if graph[child] state==goalState:
#                 return actionSequence(graph, initialState, goalState)
#                 frontier.append(child)

# solution = BFS()
# print (solution)

# actionSequence(graph, initialState, goalState):
# # returns a list of states starting from goal State moving upwards towards parent until root node is reached
# solution = [goalState]
# currentParent= graph[goalState].parent
# while currentParent!=None:
#     solution.append(currentParent)
#     currentParent = graph[currentParent].parent
# solution.reverse()
# return solution
