import math

class Node:
    def __init__(self,state,parent,action,totalCost,airCost):
        self.state=state
        self.parent=parent
        self.action=action
        self.totalCost=totalCost
        self.airCost=airCost

def findMin(frontier):
    minv=math.inf
    minNode=''
    for i in frontier:
        if minv>frontier[i][1]:
            minv=frontier[i][1]
            minNode=i
    return minNode

def actionSequence(initialState,goalState,graph):
    solution=[goalState]
    currentParent=graph[goalState].parent
    while currentParent!=None:
        solution.append(currentParent)
        currentParent=graph[currentParent].parent
    solution.reverse()
    return solution,graph[goalState].totalCost

def Astar():

    initialState='Arad'
    goalState='Bucharest'

    graph={
        'Arad' : Node('Arad', None, [('Sibiu', 140), ('Timisoara', 118), ('Zerind', 75)], 0, 366),
        'Bucharest' : Node('Bucharest', None, [('Fagaras', 211), ('Giurgiu', 90), ('Pitesti', 101), ('Urziceni', 85)], 0, 0),
        'Craiova' : Node('Craiova', None, [('Dobreta', 120), ('Pitesti', 138), ('Rimnicu Vilcea', 146)], 0, 160),
        'Dobreta' : Node('Dobreta', None, [('Craiova', 120), ('Mehadia', 75)], 0, 242),
        'Eforie' : Node('Eforie', None, [('Hirsova', 86)], 0, 161),
        'Fagaras' : Node('Fagaras', None, [('Bucharest', 211), ('Sibiu', 99)], 0, 176),
        'Giurgiu' : Node('Giurgiu', None, [('Bucharest', 90)], 0, 77),
        'Hirsova' : Node('Hirsova', None, [('Eforie', 86), ('Urziceni', 98)], 0, 151),
        'Iasi' : Node('Iasi', None, [('Neamt', 87), ('Vaslui', 92)], 0, 226),
        'Lugoj' : Node('Lugoj', None, [('Mehadia', 70), ('Timisoara', 111)], 0, 244),
        'Mehadia' : Node('Mehadia', None, [('Dobreta', 75), ('Lugoj', 70)], 0, 241),
        'Neamt' : Node('Neamt', None, [('Iasi', 87)], 0, 234),
        'Oradea' : Node('Oradea', None, [('Sibiu', 151), ('Zerind', 71)], 0, 380),
        'Pitesti' : Node('Pitesti', None, [('Bucharest', 101), ('Craiova', 138), ('Rimnicu Vilcea', 97)], 0, 100),
        'Rimnicu Vilcea' : Node('Rimnicu Vilcea', None, [('Craiova', 146), ('Pitesti', 97), ('Sibiu', 80)], 0, 193),
        'Sibiu' : Node('Sibiu', None, [('Arad', 140), ('Fagaras', 99), ('Oradea', 151), ('Rimnicu Vilcea', 80)], 0, 253),
        'Timisoara' : Node('Timisoara', None, [('Arad', 118), ('Lugoj', 111)], 0, 329),
        'Urziceni' : Node('Urziceni', None, [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)], 0, 80),
        'Vaslui' : Node('Vaslui', None, [('Iasi', 92), ('Urziceni', 142)], 0, 199),
        'Zerind' : Node('Zerind', None, [('Arad', 75), ('Oradea', 71)], 0, 374)
    }

    frontier=dict()
    frontier[initialState]=(None,0)
    explored=dict()

    while len(frontier)!=0:
        currentNode=findMin(frontier)
        del(frontier[currentNode])

        if graph[currentNode].state==goalState:
            return actionSequence(initialState,goalState,graph)

        heuristic=graph[currentNode].airCost
        currentCost=graph[currentNode].totalCost
        explored[currentNode]=(graph[currentNode].parent,currentCost+heuristic)

        for child in graph[currentNode].action:
            currentCost=child[1]+graph[currentNode].totalCost
            heuristic=graph[child[0]].airCost
            if child[0] in explored:
                if graph[child[0]].parent==currentNode or child[0]==initialState or explored[child[0]][1]<=currentCost+heuristic:
                    continue
            if child not in frontier:
                graph[child[0]].parent=currentNode
                graph[child[0]].totalCost=currentCost
                frontier[child[0]]=(graph[child[0]].parent,currentCost+heuristic)
            else:
                if frontier[child[0]][1]<=currentCost+heuristic:
                    graph[child[0]].parent=frontier[child[0]][0]
                    graph[child[0]].totalCost=frontier[child[0]][1]-heuristic
                else:
                    frontier[child[0]]=(currentNode,currentCost+heuristic)
                    graph[child[0]].parent=frontier[child[0]][0]
                    graph[child[0]].totalCost=currentCost

solution=Astar()
print(solution)