class Node(object):
    def __init__(self, students):
        self.students = students
    
    def get_students(self):
        return self.students
    
    def __str__(self):
        return self.students


class Edge(object):
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
    
    def get_source(self):
        return self.source
    
    def get_destination(self):
        return self.destination
    
    def __str__(self):
        return self.source.get_students() + ' -> ' + self.destination.get_students()


class Graph(object):
    def __init__(self):
        self.edges = {}
    
    def addNode(self, node):
        if node in self.edges:
            raise ValueError("Duplicate Node")
        else:
            self.edges[node] = []
    
    def addEdge(self, edge):
        source = edge.get_source()
        destination = edge.get_destination()
    
        if not (source in self.edges and destination in self.edges):
            raise ValueError("Node not in graph")

        n = source.get_students()
        d = destination.get_students()
        for c in range(len(n)):
            if c < (len(n)-1):
                if (n[c+1] + n[c]) == (d[c] + d[c+1]):
                    self.edges[source].append(destination)
    
    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges
    
    def getNode(self, students):
        for n in self.edges:
            if n.get_students == students:
                return n
        
        raise NameError(students)

    def __str__(self):
        result = ''
        for source in self.edges:
            for destination in self.edges[source]:
                result = result + source.get_students() + '->' + destination.get_students() + '\n'
        
        return result[:-1]


nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)


l = len(nodes)
for n1 in range(l):
    for n2 in range(l):
        if nodes[n1] != nodes[n2]:
            g.addEdge(Edge(nodes[n1], nodes[n2]))
