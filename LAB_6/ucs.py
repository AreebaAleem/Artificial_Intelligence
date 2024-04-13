import math
from queue import PriorityQueue

class Node:
    def __init__(self, name, actions=None, parent=None):
        self.name = name
        self.actions = actions if actions else []
        self.parent = parent

def UCS():
    initialState = 'C'
    goalState = 'B'

    graph = {
        'A': Node('A', [('B', 6), ('C', 9), ('E', 1)]),
        'B': Node('B', [('A', 6), ('D', 3), ('E', 4)]),
        'C': Node('C', [('A', 9), ('F', 2), ('G', 3)]),
        'D': Node('D', [('B', 3), ('E', 5), ('F', 7)]),
        'E': Node('E', [('A', 1), ('B', 4), ('D', 5), ('F', 6)]),
        'F': Node('F', [('C', 2), ('E', 6), ('D', 7)]),
        'G': Node('G', [('C', 3)])
    }

    frontier = PriorityQueue()
    frontier.put((0, initialState))
    explored = set()

    while not frontier.empty():
        currentCost, currentNode = frontier.get()

        if currentNode == goalState:
            return reconstruct_path(graph, currentNode)

        if currentNode in explored:
            continue

        explored.add(currentNode)

        for child in graph[currentNode].actions:
            childNode, stepCost = child
            if childNode not in explored:
                newCost = currentCost + stepCost
                frontier.put((newCost, childNode))
                graph[childNode].parent = currentNode

    return None  # If the goal state is not reachable

def reconstruct_path(graph, goal_node):
    path = []
    current_node = goal_node
    while current_node is not None:
        path.insert(0, current_node)
        current_node = graph[current_node].parent
    return path

solution = UCS()
if solution:
    print("Path found:", solution)
    print("Total cost:", len(solution) - 1)
else:
    print("Path not found")
