import math

class Node:
    def __init__(self, state, parent, actions, totalCost, heuristic):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost
        self.heuristic = heuristic

def hill_climbing(graph, initialState, goalState):
    current_state = initialState

    while current_state != goalState:
        current_node = graph[current_state]
        neighbors = current_node.actions
        best_neighbor = None
        best_heuristic = float('inf')  # Set to positive infinity initially

        for neighbor_state, _ in neighbors:
            neighbor_node = graph[neighbor_state]
            if neighbor_node.heuristic < best_heuristic:  # Compare with the lowest heuristic
                best_neighbor = neighbor_state
                best_heuristic = neighbor_node.heuristic

        if best_neighbor is None:
            break

        current_state = best_neighbor

    if current_state == goalState:
        return actionSequence(graph, initialState, goalState)

    return None

def actionSequence(graph, initialState, goalState):
    solution = [goalState]
    current_state = goalState

    while current_state != initialState:
        current_node = graph[current_state]
        parent_state = current_node.parent
        solution.append(parent_state)
        current_state = parent_state

    solution.reverse()
    return solution


graph = {
    'A': Node('A', None, [('F', 1)], (0, 0), 1),
    'B': Node('B', None, [('C', 1), ('G', 1)], (0, 2), 2),
            'C': Node('C', None, [('B', 1), ('D', 1)], (0, 3), 3),
        'D': Node('D', None, [('C', 1), ('E', 1)], (0, 4), 4),
        'E': Node('E', None, [('D', 1)], (0, 5), 5),
        'F': Node('F', None, [('A', 1), ('H', 1)], (1, 0), 6),
        'G': Node('G', None, [('B', 1), ('J', 1)], (1, 2), 1),
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

initialState = 'A'
goalState = 'Y'

solution = hill_climbing(graph, initialState, goalState)
print(solution)
