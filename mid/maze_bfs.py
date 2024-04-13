class Node:

    def __init__(self,state,parent,actions,cost) :
        self.state=state
        self.parent = parent
        self.actions=actions
        self.cost = cost

def actionSequence(initialState,goalState,graph):
    solution = [goalState]
    currentParent = graph[goalState].parent
    while currentParent!=None:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution

def bfs():

    initialState = "G"
    goalState = "10"

    graph = {
        "G": Node("G", None, ["5"],None),
        "1": Node("1", None, ["2","7"], None),
        "2": Node("2", None, ["1","3"], None),
        "3": Node("3", None, ["2", "4"], None),
        "4": Node("4", None, ["3", "5"], None),
        "5": Node("5", None, ["4","6"], None),
        "6": Node("6", None, ["5","8"], None),

        "7": Node("7", None, ["1","9"],None),
        "8": Node("8", None, ["6","12"], None),
        "9": Node("9", None, ["7","13"], None),
        "10": Node("10", None, ["14"], None),
        "11": Node("11", None, ["12"], None),
        "12": Node("12", None, ["8","11","15"], None),
        "13": Node("13", None, ["9","16"], None),

        "14": Node("14", None, ["10","17"],None),
        "15": Node("15", None, ["12","19"], None),
        "16": Node("16", None, ["13","20"], None),
        "17": Node("17", None, ["14","22"], None),
        "18": Node("18", None, ["19","24"], None),
        "19": Node("19", None, ["15","18","25"], None),
        "20": Node("20", None, ["16","20"], None),

        "21": Node("21", None, ["20","22"],None),
        "22": Node("22", None, ["17","21","23"], None),
        "23": Node("23", None, ["22","24"], None),
        "24": Node("24", None, ["18","23","25"], None),
        "25": Node("25", None, ["19","24"], None)
        }

    frontier = [initialState]
    explored = []

    while len(frontier)!=0:
        currentNode = frontier.pop(0)
        explored.append(currentNode)
        for child in graph[currentNode].actions:
            if child not in frontier and child not in explored:
                graph[child].parent=currentNode
            if graph[child].state == goalState:
                return actionSequence(initialState,goalState,graph)
            frontier.append(child)

solution = bfs()
print(solution)



