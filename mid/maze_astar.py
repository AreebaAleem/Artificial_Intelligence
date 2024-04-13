import math

class Node:
    def __init__(self, state, parent, actions, totalCost, air_cost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost
        self.air_cost = air_cost

def actionSequence(graph, initialState, goalState):
    solution = [goalState]
    currentParent = graph[goalState].parent
    while currentParent != None:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution, graph[goalState].totalCost

def findMin(frontier):
    minV = math.inf
    node = ''
    for i in frontier:
        if minV > frontier[i][1]:
            minV = frontier[i][1]
            node = i
    return node

def Astar():

    initialState = (0, 0)
    goalState = (9, 9)
    g, s = (9, 9)

    graph = dict()

    for i in range(10):
        for j in range(10):
            graph[i, j] = Node((i, j), None, None, 0, 0)


    maze = [['1', '2', '3', '4', '0', '6', '7', '8', '9', '10'],
            ['11', '12', '0', '14', '15', '16', '0', '0', '19', '20'],
            ['21', '22', '23', '0', '25', '26', '', '', '29', '0'],
            ['31', '0', '33', '34', '0', '36', '37', '38', '0', '0'],
            ['41', '0', '0', '44', '45', '46', '47', '48', '49', '50'],
            ['51', '0', '53', '54', '0', '0', '0', '58', '0', '0'],
            ['0', '62', '63', '0', '0', '0', '67', '68', '69', '70'],
            ['71', '0', '0', '0', '75', '76', '77', '78', '79', '80'],
            ['81', '82', '83', '0', '85', '86', '87', '88', '89', '90'],
            ['0', '92', '0', '0', '0', '96', '97', '98', '0', '100']]

    child = dict()
    for i in range(10):
        for j in range(10):
            child[i, j] = ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1))

    frontier = dict()
    frontier[initialState] = (None, 0)
    explored = dict()

    while len(frontier) != 0:
        currentNode = findMin(frontier)
        del frontier[currentNode]
        r, c = currentNode
        if currentNode == goalState:
            return actionSequence(graph, initialState, goalState)

        heuristic = math.sqrt((r - g) ** 2 + (c - s) ** 2)
        total = graph[currentNode].totalCost
        explored[currentNode] = (graph[currentNode].parent, total + heuristic)

        for childState in child[currentNode]:
            
            if not (0 <= childState[0] < 10 and 0 <= childState[1] < 10) or maze[childState[0]][childState[1]] == '0':
                continue

            childTotal = total+1
            childHeuristic = math.sqrt((childState[0] - g) ** 2 + (childState[1] - s) ** 2)

            if childState in explored:
                if graph[childState].parent == currentNode or childState == initialState or explored[childState][1] <= childTotal + childHeuristic:
                    continue

            if childState not in frontier:
                graph[childState].parent = currentNode
                graph[childState].totalCost = childTotal
                frontier[childState] = (graph[childState].parent, childTotal + childHeuristic)
            else:
                if frontier[childState][1] <= childHeuristic + childTotal:
                    graph[childState].parent = frontier[childState][0]
                    graph[childState].totalCost = frontier[childState][1] - childHeuristic
                else:
                    frontier[childState] = (currentNode, childTotal + childHeuristic)
                    graph[childState].parent = frontier[childState][0]
                    graph[childState].totalCost = childTotal

sol = Astar()
print(sol)
