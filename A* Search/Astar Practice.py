import math
import heapq

def heuristic(coordinates, node, goal):
    x1, y1 = coordinates[node]
    x2, y2 = coordinates[goal]
    return ((x2-x1)**2+(y2-y1)**2)


class NodeState:
    def __init__(self, node, g, f, parent=None):
        self.node = node
        self.g = g
        self.f = f
        self.parent = parent

    
    def __lt__(self, other):
        return self.f<other.f
    

def AstarSearch(coordinates, adjList, start, goal):
    minPq = []
    startHeuristic = heuristic(coordinates, start, goal)
    startNodeState = NodeState(start, 0, startHeuristic)
    best_g = {start: 0}
    bestPath = None
    bestCost = float('inf') 
    heapq.heappush(minPq, startNodeState)

    while minPq:
        currentState = heapq.heappop(minPq)
        if currentState.g>best_g[currentState.node]:
            continue

        if currentState.node == goal:
            if currentState.g<bestCost:
                bestCost = currentState.g
                path = []
                tempState = currentState
                while tempState:
                    path.append(tempState.node)
                    tempState = tempState.parent
                path.reverse()
                bestPath = path 
            continue

        for neighbour, edgeCost in adjList[currentState.node]:
            new_g = currentState.g + edgeCost
            if neighbour not in best_g or new_g < best_g[neighbour]:
                best_g[neighbour] = new_g
                h = heuristic(coordinates, neighbour, goal)
                f = new_g + h
                nextState = NodeState(neighbour, new_g, f, currentState)
                heapq.heappush(minPq, nextState)
    
    return (bestPath, bestCost) if bestPath else (None, -1)


def takeInput():
    coordinates = {}
    adjList = {}
    with open('input.txt', 'r') as f:
        nodes = int(f.readline())
        for i in range(nodes):
            line = f.readline().split()
            coordinates[line[0]] = (int(line[1]), int(line[2]))
            adjList[line[0]] = []
        
        edges = int(f.readline())
        for i in range(edges):
            line = f.readline().split()
            start, end, cost = line[0], line[1], int(line[2])
            adjList[start].append((end, cost)) 
        
        start = f.readline().strip()
        goal  = f.readline().strip()

    return coordinates, adjList, start, goal


coordinates, adjList, start, goal = takeInput()
solutionPath, solutionCost = AstarSearch(coordinates, adjList, start, goal)
if solutionPath:
    print("Solution path:", " -> ".join(solutionPath))
    print("Solution cost:", solutionCost)
else:
    print("No path exists.")