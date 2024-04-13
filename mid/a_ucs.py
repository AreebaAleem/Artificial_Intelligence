import math

class Node:
    def __init__(self,state,parent,action,totalCost):
        self.state=state
        self.parent=parent
        self.action=action
        self.totalCost=totalCost

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
    return solution

def UCS():

    initialState='C'
    goalState='B'

    graph={
        'A': Node('A',None,[('B',6),('E',1),('C',9)],0),
        'B': Node('B',None, [('A',6),('D',3),('E',4)],0),
        'C': Node('C',None, [('A',9),('F',2),('G',3)],0),
        'D': Node('D',None, [('B',3),('E',5),('F',7)],0),
        'E': Node('E',None, [('A',1),('B',4),('D',5),('F',6)],0),
        'F': Node('F',None, [('C',6),('D',7),('E',6)],0),
        'G': Node('G',None, [('C',3)],0)
    }

    frontier=dict()
    frontier[initialState]=(None,0)
    explored=[]

    while len(frontier)!=0:
        currentNode=findMin(frontier)
        del(frontier[currentNode])
        explored.append(currentNode)
        if graph[currentNode].state==goalState:
            return actionSequence(initialState,goalState,graph)
        for child in graph[currentNode].action:
            currentCost=child[1]+graph[currentNode].totalCost
            if child[0] not in frontier and child[0] not in explored:
                graph[child[0]].parent=currentNode
                graph[child[0]].totalCost=currentCost
                frontier[child[0]]=(graph[child[0]].parent,graph[child[0]].totalCost)
            elif child[0] in frontier:
                if frontier[child[0]][1]<currentCost:
                    graph[child[0]].parent=frontier[child[0]][0]
                    graph[child[0]].totalCost=frontier[child[0]][1]
                else:
                    frontier[child[0]]=(currentNode,currentCost)
                    graph[child[0]].parent=frontier[child[0]][0]
                    graph[child[0]].totalCost=frontier[child[0]][1]

solution=UCS()
print(solution)