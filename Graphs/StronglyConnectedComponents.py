import operator
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
t = 0
s = None
leaders = {}
numbers = open("./SCC.txt", "r")
reversedGraph = Directedgraph()
normalGraph = Directedgraph()
for line in numbers:
    u, v = [int(x) for x in line.split()]
    reversedGraph.add_edge(v, u)
    normalGraph.add_edge(u, v)
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
        if not G.vertices[i].explored:
            if not pass1:
                s = i
                leaders[i] = 0
            DFS(G.vertices[i], pass1)
    if pass1:
        normalGraph.vertices = normalGraph.time_vertices.copy()
        del normalGraph.time_vertices
""" print("normal")
normalGraph.get_edges()
print("reversed")
reversedGraph.get_edges() """
DFS_loop(reversedGraph, True)
DFS_loop(normalGraph, False)
output = open("result.txt", "w")
for val in leaders.values():
    output.write(str(val)+" ")