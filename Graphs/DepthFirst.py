class Vertice:
    def __init__(self, val):
        self.history = []
        self.value = val
        self.adjacent = []
    def addAdjacent(self, adj):
        self.adjacent.append(adj)
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
def DepthWiseSearch(g, start, end):
    work = []
    visited = set()
    start.history = []
    work.append(start)
    visited.add(start)
    while len(work):
        current = work.pop()
        if (current == end):
            current.history.append(current)
            return current.history.copy()
        else:
            neighbors = current.adjacent
            for neighbor in neighbors:
                if neighbor not in visited:
                    neighbor.history = current.history.copy()
                    neighbor.history.append(current)
                    work.append(neighbor)
                    visited.add(neighbor)
    return None
        
graphRep = open("./simpleGraph.txt", "r")
graph = Graph()
for line in graphRep:
    result = [int(x) for x in line.split()]
    graph.addEdge(result[0], result[1])
print([x.value for x in DepthWiseSearch(graph, graph.vertices[1], graph.vertices[5])])