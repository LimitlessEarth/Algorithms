import sys
sys.setrecursionlimit(100000)

count = 1
sccnodes = 0
sccedges = 0

class Vertex:
	def __init__(self, key):
       	 	self.id = key
        	self.connectedTo = {}
		self.visited = False
		self.svisit = False
		self.previsit = 0
		self.postvisit = 0
	
	def addchild(self, chld, weight = 0):
		self.connectedTo[chld] = weight

	def getConnections(self):
        	return self.connectedTo.keys()
	
	def getId(self):
        	return self.id

class Graph:
	def __init__(self):
		self.vertList = {}
		self.numVertices = 0
		self.post = []

	def addVertex(self, key):
		newVertex = Vertex(key)
		self.vertList[key] = newVertex
		return newVertex

  	def getVertex(self, n):
        	if n in self.vertList:
            		return self.vertList[n]
        	else:
           		return None

	def addEdge(self, f, t, cost = 0):
		self.vertList[f].addchild(self.vertList[t], cost)

	def __contains__(self,n):
        	return n in self.vertList

	def __iter__(self):
	        return iter(self.vertList.values())

def MakeRGraph(graph):
	
	global sccnodes, sccedges

	snmax = 0
	scmax = 0

	g = Graph()
	gr = Graph()

	a = open(graph, "r")
	graph = a.read().splitlines()
	a.close()

	for i in range(0,77361):
		g.addVertex(i)
		gr.addVertex(i)	

	for line in graph:
		graphu = line.split("\t")
		gr.addEdge(int(graphu[1]), int(graphu[0]), 0)
		g.addEdge(int(graphu[0]), int(graphu[1]), 0)

	dfs(gr)
	
	gr.post.reverse()
	g.post = gr.post

	for p in g.post:
		sccnodes = 0
		sccedges = 0
		explorescc(g, g.getVertex(p))
		if sccnodes > snmax:
			snmax = sccnodes
			semax = sccedges

	print snmax
	print semax

			


	
def dfs(gr):
	
	global count

	for v in gr:
		if v.visited == False:
			count = 0
			explore(gr, v)
			gr.post.append(v.getId())

	return gr

def explore(gr, v):
	
	v.visited = True
	previsit(v)

	if v.getConnections():
		for e in v.getConnections():
			if e.visited == False:
				explore(gr, e)
	postvisit(v) 


def explorescc(g, v):
	
	v.svisit = True
	nodes()
	if v.getConnections():
		for e in v.getConnections():
			edges()
			if e.svisit == False:
				explorescc(g, e)
	
def previsit(v):
	global count
	v.previsit = count
	count += 1


def postvisit(v):
	global count
	v.postvisit = count
	count += 1

def nodes():
	global sccnodes
	sccnodes += 1
	
def edges():
	global sccedges
	sccedges += 1



		
        	

MakeRGraph("soc-Slashdot0811.txt")

# Largest SCC number of nodes = 70361
# Largest SCC number of edges = 897918








