
class Node:
    def __init__(self, name, actions=None, parent=None):
        self.name = name
        self.actions = actions if actions else []
        self.parent = parent

def BFS():
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
        # returns a list of states starting from goal State moving upwards towards parent until the root node is reached
        solution = [goalState]
        currentParent = graph[goalState].parent
        while currentParent:
            solution.append(currentParent)
            currentParent = graph[currentParent].parent
        solution.reverse()
        return solution

    while frontier:
        currentNode = frontier.pop(0)
        explored.append(currentNode)
        for child in graph[currentNode].actions:
            if child not in frontier and child not in explored:
                graph[child].parent = currentNode
                if child == goalState:
                    return actionSequence(graph, initialState, goalState)
                frontier.append(child)

solution = BFS()
print(solution)


# def BFS():
#     initialState='s'
#     goalState='g'


# graph={
#     's':Node('s',None['d','e','p'],None),
#     'a':Node('a',None),
#     'b':Node('b',None['A'],None),
#     'c':Node('c',None['A'],None),
#     'd':Node('d',None['B','C','E'],None),
#     'e':Node('e',None['H','R'],None),
#     'f':Node('f',None['C','G'],None),
#     'g':Node('g',None),
#     'h':Node('h',None['P','Q'],None),
#     'p':Node('p',None['Q'],None),
#     'q':Node('q',None),
#     'r':Node('r',None['F'],None)
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
