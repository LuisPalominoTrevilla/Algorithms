class Vertice:
    def __init__(self, val):
        self.history = []
        self.value = val
        self.adjacent = []
        self.prev = None
    def addAdjacent(self, adj, weight):
        self.adjacent.append((adj, weight))
class Graph:
    def __init__(self):
        self.vertices = {}
        self.entering = {}
    def addEdge(self, u, v, weight):
        if u not in self.vertices:
            self.vertices[u] = Vertice(u)
        if v not in self.vertices:
            self.vertices[v] = Vertice(v)
        if v not in self.entering:
            self.entering[v] = 0
        self.vertices[u].addAdjacent(self.vertices[v], weight)
        self.entering[v] += 1
    def printEdges(self):
        for vertex in self.vertices:
            neighbors = self.vertices[vertex].adjacent
            for (neighbor, w) in neighbors:
                print("FROM ", self.vertices[vertex].value, " to ", neighbor.value, " weight ", w)
class Node:
    def __init__(self, val):
        self.value = val
        self.adjacent = []
        self.explored = False
    def add_adjacent(self, node):
        self.adjacent.append(node)
class Directedgraph:
    def __init__(self):
        self.vertices = {}
    def add_edge(self, u, v):
        if u not in self.vertices:
            self.vertices[u] = Node(u)
        if v not in self.vertices:
            self.vertices[v] = Node(v)
        self.vertices[u].add_adjacent(self.vertices[v])
    def get_edges(self):
        for vertice in self.vertices.keys():
            for adjacent in self.vertices[vertice].adjacent:
                print("[",vertice,"] val=", self.vertices[vertice].value, " => ", adjacent.value)
    def generate_time_ordered_vertices(self):
        self.time_vertices = {}
import numpy as np
M = np.matrix([[0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0],
              [7,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,-1,0,3,0,0,0,0,3,0,0,0,0,0,0],
              [0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,-4,0,1,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,5,0,0,0,3,1,0,0,0,0,0,0,0],
              [0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0],
              [0,0,0,0,0,-4,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,1],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,1],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,-4,0,0,1],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              ])
def countCycles(start, isPositive):
    visited = set()
    work = []
    numLoops = 0
    work.append(start)
    sumCycle = 0
    all_cicles = []
    curr_cicle = []
    unconected = set()
    curr_cicle.append(start.value)
    while len(work):
        current = work.pop()
        visited.add(current)
        neighbors = current.adjacent
        if len(neighbors) == 0:
            unconected.add(current)
            continue
        for (neighbor, w) in neighbors:
            if neighbor in unconected:
                continue
            if neighbor not in visited:
                if neighbor not in work:
                    neighbor.prev = (current, w)
                    work.append(neighbor)
            else:
                curr_cicle = [current.value]
                (tmp, weight) = current.prev
                sumCycle += weight + w
                unconected.add(tmp)
                while tmp.value != neighbor.value:
                    curr_cicle.append(tmp.value)
                    (tmp, weight) = tmp.prev
                    sumCycle += weight
                    unconected.add(tmp)
                curr_cicle.append(tmp.value)
                if isPositive:
                    if (sumCycle >= 0):
                        all_cicles.append(curr_cicle)
                else:
                    if (sumCycle < 0):
                        all_cicles.append(curr_cicle)
                numLoops += 1
                sumCycle = 0
                curr_cicle = []
    return (numLoops, all_cicles)
def positiveCycles(g):
    numCycles = 0
    loops = []
    for vertex in g.vertices:
        res = countCycles(g.vertices[vertex], True)
        numCycles += res[0]
        for x in res[1]:
            loops.append(x)
    loops.sort()
    for mini in loops:
        mini.sort()
    res = []
    numCycles = 0
    for loop in loops:
        if loop not in res:
            res.append(loop)
            numCycles += 1
    return (numCycles, res)
def negativeCycles(g):
    numCycles = 0
    loops = []
    for vertex in g.vertices:
        res = countCycles(g.vertices[vertex], False)
        numCycles += res[0]
        for x in res[1]:
            loops.append(x)
    loops.sort()
    for mini in loops:
        mini.sort()
    res = []
    numCycles = 0
    for loop in loops:
        if loop not in res:
            res.append(loop)
            numCycles += 1
    return (numCycles, res)
# Change graph representation to an adjacency list

t = 0
s = None
leaders = {}
reversedGraph = Directedgraph()
normalGraph = Directedgraph()
for i in range(M.shape[0]):
    for j in range(M.shape[1]):
        w = M.item(i,j)
        if w != 0:
            reversedGraph.add_edge(j+1, i+1)
            normalGraph.add_edge(i+1, j+1)
reversedGraph.add_edge(14, 14)
normalGraph.add_edge(14,14)
def DFS(i, pass1):
    global t
    global s
    if pass1:
        global normalGraph
    else:
        global leaders
    work = []
    visited = []
    work.append(i)
    while len(work) > 0:
        current = work.pop()
        if current.explored: continue
        current.explored = True
        visited.append(current)
        if not pass1:
            leaders[s] += 1
        for adj in current.adjacent:
            if not adj.explored:
                work.append(adj)
    if pass1:
        while len(visited)>0:
            t+=1
            current = visited.pop().value
            normalGraph.time_vertices[t] = normalGraph.vertices[current]
def DFS_loop(G, pass1):
    global t
    global s
    if pass1:
        global normalGraph
        normalGraph.generate_time_ordered_vertices()
    else:
        global leaders
    t = 0
    s = None
    for i in range(len(G.vertices), 0, -1):
        if not pass1:
            s = i
            leaders[i] = 0
        DFS(G.vertices[i], pass1)
    if pass1:
        normalGraph.vertices = normalGraph.time_vertices.copy()
        del normalGraph.time_vertices
DFS_loop(reversedGraph, True)
DFS_loop(normalGraph, False)
print("Lider componente fuertemente conectado -> numero de elementos en el cluster conectados")
for val in leaders:
    print(normalGraph.vertices[val].value, " -> ", leaders[val])