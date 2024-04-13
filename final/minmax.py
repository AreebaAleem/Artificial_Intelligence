import math
MAX = math.inf
MIN = math.inf * -1

def max_value(depth, nodeIndex, values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]

    v = MIN
    for i in range(0, 2):
        val = min_value(depth + 1, nodeIndex * 2 + i, values, alpha, beta)
        v = max(v, val)
        alpha = max(alpha, v)

        if beta <= alpha:
            break

    return v

def min_value(depth, nodeIndex, values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]

    v = MAX
    for i in range(0, 2):
        val = max_value(depth + 1, nodeIndex * 2 + i, values, alpha, beta)
        v = min(v, val)
        beta = min(beta, v)

        if beta <= alpha:
            break

    return v

def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    if maximizingPlayer:
        return max_value(depth, nodeIndex, values, alpha, beta)
    else:
        return min_value(depth, nodeIndex, values, alpha, beta)

if __name__ == "__main__":
    values = [2,3,5,9,0,1,7,5]
    print("The optimal value is:", minimax(0, 0, True, values, MIN, MAX))

# import math
# MAX = math.inf
# MIN = math.inf * -1

# def max_value(depth, nodeIndex, values):
#     if depth == 3:
#         return values[nodeIndex]

#     v = MIN
#     for i in range(0, 2):
#         val = min_value(depth + 1, nodeIndex * 2 + i, values)
#         v = max(v, val)



#     return v

# def min_value(depth, nodeIndex, values):
#     if depth == 3:
#         return values[nodeIndex]

#     v = MAX
#     for i in range(0, 2):
#         val = max_value(depth + 1, nodeIndex * 2 + i, values)
#         v = min(v, val)

   

#     return v

# def minimax(depth, nodeIndex, maximizingPlayer, values):
#     if maximizingPlayer:
#         return max_value(depth, nodeIndex, values)
#     else:
#         return min_value(depth, nodeIndex, values)

# if __name__ == "__main__":
#     values = [2,3,5,9,0,1,7,5]
#     print("The optimal value is:", minimax(0, 0, True, values))