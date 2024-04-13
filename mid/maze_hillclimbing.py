import math

class Node:
    def __init__(self, state, parent, neighbors, heuristic, totalCost):
        self.state = state
        self.parent = parent
        self.neighbors = neighbors
        self.heuristic = heuristic
        self.totalCost = totalCost

def HillClimbing(maze):
    def get_neighbors(node_state):
        x, y = node_state
        return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

    def is_valid_move(node_state):
        x, y = node_state
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '0'

    graph = {}
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if maze[x][y] != '':
                neighbors = [neighbor for neighbor in get_neighbors((x, y)) if is_valid_move(neighbor)]
                graph[(x, y)] = Node((x, y), None, neighbors, (x, y), 0)

    initialState = (0, 0)
    goalState = (len(maze) - 1, len(maze[0]) - 1)

    parentNode = initialState
    parentCost = math.sqrt((graph[goalState].heuristic[0] - graph[initialState].heuristic[0]) ** 2 +
                          (graph[goalState].heuristic[1] - graph[initialState].heuristic[1]) ** 2)

    explored = []
    solution = []

    while parentNode != goalState:
        bestNode = parentNode
        minChildCost = parentCost
        explored.append(parentNode)

        for child in graph[parentNode].neighbors:
            if child not in explored:
                childCost = math.sqrt((graph[goalState].heuristic[0] - graph[child].heuristic[0]) ** 2 +
                                     (graph[goalState].heuristic[1] - graph[child].heuristic[1]) ** 2)

                if childCost < minChildCost:
                    bestNode = child
                    minChildCost = childCost

        if bestNode == parentNode:
            break
        else:
            parentNode = bestNode
            parentCost = minChildCost
            solution.append(parentNode)

    return solution

maze = [
    ['1', '2', '3', '4', '0', '6', '7', '8', '9', '10'],
    ['11', '12', '0', '14', '15', '16', '0', '0', '19', '20'],
    ['21', '22', '23', '0', '25', '26', '', '', '29', '0'],
    ['31', '0', '33', '34', '0', '36', '37', '38', '0', '0'],
    ['41', '0', '0', '44', '45', '46', '47', '48', '49', '50'],
    ['51', '0', '53', '54', '0', '0', '0', '58', '0', '0'],
    ['0', '62', '63', '0', '0', '0', '67', '68', '69', '70'],
    ['71', '0', '0', '0', '75', '76', '77', '78', '79', '80'],
    ['81', '82', '83', '0', '85', '86', '87', '88', '89', '90'],
    ['0', '92', '0', '0', '0', '96', '97', '98', '0', '100']
]

solution = HillClimbing(maze)
print(solution)
