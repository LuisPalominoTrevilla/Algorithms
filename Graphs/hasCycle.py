class Vertice:
    def __init__(self, val):
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
graphRep = open("./simpleGraph.txt", "r")
graph = Graph()
for line in graphRep:
    result = [int(x) for x in line.split()]
    graph.addEdge(result[0], result[1])
def countCycles(start):
    work = []
    numLoops = 0
    visited = set()
    work.append(start)
    while len(work):
        current = work.pop()
        visited.add(current)
        neighbors = current.adjacent
        numRep = 0
        for neighbor in neighbors:
            if neighbor not in visited:
                if neighbor not in work:
                    work.append(neighbor)
            else:
                numRep += 1
                if numRep > 1:
                    numLoops += 1
    return numLoops
print(countCycles(graph.vertices[1]))