class Node:
    def __init__(self,state,parent,action,totalCost):
        self.state=state
        self.parent=parent
        self.action=action
        self.totalCost=totalCost

def BFS():

        initialState='D'
        goalState='F'

        graph={
            'A':Node('A',None,['B','C','E'],None),
            'B':Node('B',None,['A','D','E'],None),
            'C':Node('C',None,['A','F','G'],None),
            'D':Node('D',None,['B','E'],None),
            'E':Node('E',None,['A','B','D'],None),
            'F':Node('F',None,['C'],None),
            'G':Node('G',None,['C'],None),
        }

        frontier=[initialState]
        explored=[]

        while len(frontier)!=0:
            currentNode=frontier.pop(0)
            explored.append(currentNode)
            for child in graph[currentNode].action:
                if child not in frontier and child not in explored:
                    graph[child].parent=currentNode
                    if graph[child].state==goalState:
                        return actionSequence(initialState,goalState,graph)
                    frontier.append(child)

def actionSequence(initialState,goalState,graph):
            solution=[goalState]
            currentParent=graph[goalState].parent
            while currentParent!=None:
                solution.append(currentParent)
                currentParent=graph[currentParent].parent
            solution.reverse()
            return solution

solution=BFS()
print(solution)