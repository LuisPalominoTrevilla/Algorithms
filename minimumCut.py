from random import randint
class Vertice:
    def __init__(self, val):
        self.values = []
        self.values.append(val)
        self.adjacent = []
    def addValue(self, val):
        self.values.append(val)
    def addAdjacent(self, adj):
        self.adjacent.append(adj)
class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []
    def addEdge(self, u, v):
        if u not in self.vertices:
            self.vertices[u] = Vertice(u)
        if v not in self.vertices:
            self.vertices[v] = Vertice(v)
        self.vertices[u].addAdjacent(self.vertices[v])
        if [v, u] not in self.edges:
            self.edges.append([u,v])
    def getEdges(self):
        for edge in self.edges:
            print(edge[0], " -> ", edge[1])
    def contract(self):
        contractedEdges = [x.copy() for x in self.edges]
        numVertices = len(self.vertices)
        while numVertices > 2:
            curr_edge = contractedEdges[randint(0, len(contractedEdges)-1)]
            contractedEdges.remove(curr_edge)
            numVertices-=1
            #print(curr_edge)
            u = curr_edge[0]
            v = curr_edge[1]
            #self.vertices[u].adjacent.remove(self.vertices[v])
            self.vertices[u].adjacent = list(filter(lambda a: a != self.vertices[v], self.vertices[u].adjacent))
            for vertice in self.vertices[v].adjacent:
                if vertice is not self.vertices[u]:
                    # Add neighbor from v to u
                    self.vertices[u].adjacent.append(vertice)
                    # Change references to v's neighbors from v to u
                    vertice.adjacent = [x if x != self.vertices[v] else self.vertices[u] for x in vertice.adjacent]
            self.vertices[u].values.extend(self.vertices[v].values)
            self.vertices[v] = None
            remove = []
            for edge in contractedEdges:
                if edge[0] == v:
                    edge[0] = u
                elif edge[1] == v:
                    edge[1] = u
                if edge[0] == edge[1]:
                    remove.append(edge)
            for r in remove:
                contractedEdges.remove(r)
            #print("And the edges are ",contractedEdges)
        A = self.vertices[contractedEdges[0][0]].values
        B = self.vertices[contractedEdges[0][1]].values
        cuts = 0
        for u in A:
            for v in B:
                if [u,v] in self.edges or [v,u] in self.edges:
                    cuts += 1
        return cuts

numbers = open("./test.txt", "r")
adjacencyList = Graph()
for line in numbers:
    values = line.split()
    u = int(values[0])
    for i in range(1, len(values)):
        v = int(values[i])
        adjacencyList.addEdge(u, v)
#adjacencyList.getEdges()
n = 4000
min_cut = 1000000
for i in range(n):
    print(i)
    numbers = open("./kargerMinCut.txt", "r")
    adjacencyList = Graph()
    for line in numbers:
        values = line.split()
        u = int(values[0])
        for i in range(1, len(values)):
            v = int(values[i])
            adjacencyList.addEdge(u, v)
    res = adjacencyList.contract()
    if res < min_cut:
        min_cut = res
print(min_cut)
