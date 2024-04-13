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

    initialState='a'
    goalState='z'

    graph={
        'a':Node('a',None,[('b',4),('c',3)],0,14),
        'b':Node('b',None,[('a',4),('e',12),('f',5)],0,12),
        'c':Node('c',None,[('a',3),('d',7),('e',10)],0,11),
        'd':Node('d',None,[('c',7),('e',2)],0,6),
        'e':Node('e',None,[('b',12),('c',10),('z',5)],0,4),
        'f':Node('f',None,[('b',5),('z',16)],0,11),
        'z':Node('z',None,[('f',16),('e',5)],0,0),
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