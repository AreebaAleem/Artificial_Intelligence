class Puzzle:
    def __init__(self, state, parent, heuristic):
        self.state = state
        self.parent = parent
        self.heuristic = heuristic

def get_empty(array, value):
    for i, row in enumerate(array):
        if value in row:
            return i, row.index(value)
    return None, None

def get_heuristic(state, goal_state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j] and state[i][j] != 0:
                goal_i, goal_j = get_empty(goal_state, state[i][j])
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

def children(node, goal_state):
    child = []
    i, j = get_empty(node.state, 0)
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for move in moves:
        new_i, new_j = i + move[0], j + move[1]
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row[:] for row in node.state]
            new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
            heuristic = get_heuristic(new_state, goal_state)
            child.append(Puzzle(new_state, node, heuristic))
    return child

def hill_climbing(initial_state, goal_state):
    initial_heuristic = get_heuristic(initial_state, goal_state)
    current_node = Puzzle(initial_state, None, initial_heuristic)

    while True:
        child = children(current_node, goal_state)
        if not child:
            break

        best_child = min(child, key=lambda x: x.heuristic)
        if best_child.heuristic >= current_node.heuristic:
            break

        current_node = best_child

    path = []
    while current_node:
        path.append(current_node.state)
        current_node = current_node.parent

    path.reverse()
    return path

initial_state = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]
]

goal_state = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

solution_path = hill_climbing(initial_state, goal_state)

for step, state in enumerate(solution_path):
    print(f"Step {step}:")
    for row in state:
        print(row)
    print("----------")

print(f"Goal State achieved after {step} iterations.")