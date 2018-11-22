class Vertice:
    def __init__(self, val):
        self.value = val
        self.adjacent = []
        self.key = None
    def addAdjacent(self, adj):
        self.adjacent.append(adj)
    def paintKey(self, key):
        self.key = key
class Graph:
    def __init__(self):
        self.vertices = {}
    def addEdge(self, u, v):
        if u not in self.vertices:
            self.vertices[u] = Vertice(u)
        if v not in self.vertices:
            self.vertices[v] = Vertice(v)
        self.vertices[u].addAdjacent(self.vertices[v])
        self.vertices[v].addAdjacent(self.vertices[u])
    def getEdges(self):
        for key in self.vertices:
            for neighbor in self.vertices[key].adjacent:
                print(self.vertices[key].value, " -> ", neighbor.value)
def DepthWiseSearch(g, start, key):
    work = []
    visited = set()
    work.append(start)
    visited.add(start)
    while len(work):
        current = work.pop()
        current.paintKey(key)
        neighbors = current.adjacent
        for neighbor in neighbors:
            if neighbor not in visited:
                work.append(neighbor)
                visited.add(neighbor)
    return None
def connectedComponents(graph):
    count = 0
    for key in graph.vertices:
        if graph.vertices[key].key is None:
            DepthWiseSearch(graph, graph.vertices[key], count)
            count += 1
graphRep = open("./simpleGraph.txt", "r")
graph = Graph()
for line in graphRep:
    result = [int(x) for x in line.split()]
    graph.addEdge(result[0], result[1])
connectedComponents(graph)
for k in graph.vertices:
    print(graph.vertices[k].value, " is ", graph.vertices[k].key)