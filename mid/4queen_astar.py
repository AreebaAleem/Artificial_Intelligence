import random

def fitness(board):
    conflicts = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
                conflicts += 1
    return conflicts

def heuristic(board):
    return fitness(board)

def generate_neighbors(board):
    neighbors = []
    for i in range(4):
        for j in range(1, 5):
            if board[i] != j:
                neighbor_board = board[:]
                neighbor_board[i] = j
                neighbors.append(neighbor_board)
    return neighbors

def findMin(frontier):
    min_priority = float('inf')
    min_state = None
    for priority, state in frontier:
        if priority < min_priority:
            min_priority = priority
            min_state = state
    return min_state

def AStarQueens():
    initial_board = [1, 2, 3, 4]
    goal_fitness = 0

    frontier = [(heuristic(initial_board), initial_board)]

    explored = set()

    while frontier:
        current_board = findMin(frontier)
        frontier = [state for state in frontier if state[1] != current_board]
        explored.add(tuple(current_board))

        if fitness(current_board) == goal_fitness:
            return current_board

        print("Current State:", current_board)

        neighbors = generate_neighbors(current_board)
        print("Neighbor States:")
        for neighbor in neighbors:
            if tuple(neighbor) not in explored:
                priority = heuristic(neighbor)
                print(f"Neighbor: {neighbor}, Heuristic: {priority}")
                frontier.append((priority, neighbor))

    return None

solution = AStarQueens()
if solution:
    print("Solution found:")
    print("Final State:", solution)
else:
    print("No solution found. Try again.")
