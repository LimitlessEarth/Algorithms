import Queue
import sys
sys.setrecursionlimit(100000)

class Vertex:
	def __init__(self, key):
       	 	self.id = key
        	self.connectedTo = {}
		self.dist = 1000000000
		self.visited = False
	
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

def MakeRGraph(graph, n):
	
	longest = 0

	g = Graph()

	a = open(graph, "r")
	graph = a.read().splitlines()
	a.close()

	for i in range(0,n + 1):
		g.addVertex(i)	

	for line in graph:
		graphu = line.split("\t")
		g.addEdge(int(graphu[0]), int(graphu[1]), 0)


	for s in g:
		m = bfs(g, s)
		for a in g:
			a.dist = 1000000000
		if m > longest:
			longest = m
	print longest
		

def bfs(g, s):
	
	s.dist = 0
	maxdist = 0
	
	Q = Queue.Queue(maxsize=0)
	Q.put(s)
	
	while not Q.empty():
		u = Q.get()
		for e in u.getConnections():
			if e.dist > 999999999:
				Q.put(e)
				e.dist = u.dist + 1
				if e.dist > maxdist:
					maxdist = e.dist
	return maxdist
				





		
MakeRGraph("soc-Slashdot0811.txt", 77360)

# Diameter = 10








