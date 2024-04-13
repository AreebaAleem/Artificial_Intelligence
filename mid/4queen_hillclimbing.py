import random

def fitness(board):
    conflicts = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
                conflicts += 1
    return conflicts

def hillClimbingQueens():
    board = [random.randint(1, 4) for _ in range(4)]
    iterations = 0

    while True:
        current_fitness = fitness(board)
        print(f"Iteration {iterations}:")
        print("Current State:", board)
        print(f"Current Fitness: {current_fitness}\n")

        if current_fitness == 0:
            return board

        neighbors = []

        for i in range(4):
            for j in range(1, 5):
                if board[i] != j:
                    neighbor_board = board[:]
                    neighbor_board[i] = j
                    neighbors.append(neighbor_board)

        best_neighbor = min(neighbors, key=fitness)
        best_fitness = fitness(best_neighbor)

        print("Neighbors:")
        for neighbor in neighbors:
            print("State:", neighbor)
            print(f"Fitness: {fitness(neighbor)}")

        print("\nBest Neighbor:")
        print("State:", best_neighbor)
        print(f"Best Fitness: {best_fitness}\n")

        if best_fitness >= current_fitness:
            return None
        else:
            board = best_neighbor

        iterations += 1

solution = hillClimbingQueens()
if solution:
    print("Solution found:")
    print("Final State:", solution)
else:
    print("No solution found. Try again.")
