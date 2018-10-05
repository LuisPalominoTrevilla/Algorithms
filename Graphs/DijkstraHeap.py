from MinHeap import MinHeap
class Node:
    def __init__(self, val):
        self.value = val
        self.adjacent = []
        self.key = None
    def add_adjacent(self, node, weigth):
        self.adjacent.append((node, weigth))
    def setKey(self, key):
        self.key = key
class Weightedgraph:
    def __init__(self):
        self.vertices = {}
    def add_edge(self, u, v, weigth):
        if u not in self.vertices:
            self.vertices[u] = Node(u)
        if v not in self.vertices:
            self.vertices[v] = Node(v)
        self.vertices[u].add_adjacent(self.vertices[v], weigth)
    def get_edges(self):
        for vertice in self.vertices.keys():
            for adjacent in self.vertices[vertice].adjacent:
                print(self.vertices[vertice].value, " => ", adjacent[1], " =>", adjacent[0].value)
def DijkstraHeap(graph, s, heap):
    keys = {0: [s]}
    X = set()
    s.setKey(0)
    X.add(s)
    for adj in s.adjacent:
        adj[0].setKey(adj[1])
        if adj[1] not in keys:
            keys[adj[1]] = []
        keys[adj[1]].append(adj[0])
        heap.insert(adj[1])
    while(not heap.isEmpty()):
        w = keys[heap.extractMin()][0]
        keys[w.key].remove(w)
        X.add(w)
        for adj in w.adjacent:
            v = adj[0]
            l = adj[1]
            if v not in X:
                if v.key is not None:
                    heap.extractElement(v.key)
                    keys[v.key].remove(v)
                    v.key = min(v.key, w.key+l)
                else:
                    v.key = l + w.key
                if v.key not in keys:
                    keys[v.key] = []
                keys[v.key].append(v)
                heap.insert(v.key)
    for node in X:
        print(node.value, " min path: ", node.key)

numbers = open("./weightedGraph.txt", "r")
graph = Weightedgraph()
for line in numbers:
    results = line.split()
    u = int(results[0])
    for i in range(1, len(results)):
        v, weight = [int(x) for x in results[i].split(',')]
        graph.add_edge(u, v, weight)
heap = MinHeap()
DijkstraHeap(graph, graph.vertices[1], heap)