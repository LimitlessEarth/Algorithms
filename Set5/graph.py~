import sys

class Vertex:
	def __init__(self, key):
       	 	self.id = key
        	self.connectedTo = {}
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

	def addVertex(self, key):
		self.numVerticies = self.numVertices + 1
		newVertex = Vertex(key)
		self.vertList[key] = newVertex
		return newVertex

  	def getVertex(self, n):
        	if n in self.vertList:
            		return self.vertList[n]
        	else:
           		return None

	def addEdge(self, f, t, cost = 0):
		if f not in self.vertList:
           		nv = self.addVertex(f)
        	if t not in self.vertList:
           		nv = self.addVertex(t)
		self.vertList[f].addchild(self.vertList[t], cost)

	def __contains__(self,n):
        	return n in self.vertList

	def __iter__(self):
	        return iter(self.vertList.values())



def makeGraph(sortedlist):

	a = open(sortedlist,"r")
	sortedlist = a.read().splitlines()
	a.close()

	g = Graph()
	l = len(sortedlist)

	for f in range(0, l):
		g.addVertex(sortedlist[f])


	for i in range(0, l):
		b = sortedlist[i]
		c = list(b)
		sys.stdout.write(" %s" % i)
		for j in range(0, l):
			d = sortedlist[j]
			e = list(d)
			sublist = [x for x in c if x not in e]
			if len(sublist) == 0:
				g.addEdge(sortedlist[i], sortedlist[j], 1)
			
		e = "".join(d)

	return g

def dfs(g):

	Max = 0	

	for v in iter(g):
		if v.visited == False:
			Current = explore(g, v, 0)
			#sys.stdout.write(" %s" % Current)
			if Current > Max:
				Max = Current
	sys.stdout.write(" %s" % Max)

def explore(g, v, Counter):

	v.visited = True
	for e in v.getConnections():
		if e.visited == False:
			return explore(g, e, Counter + 1)

	#sys.stdout.write(" %s" % Counter)
	return Counter
	
				
	
dfs(makeGraph("sortedlist.txt"))
				
		
	



