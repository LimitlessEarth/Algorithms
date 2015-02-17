import Queue
import sys
import threading

longest = 0

class myThread (threading.Thread):
    def __init__(self, threadID, graphname, vertex):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.graphname = graphname
        self.vertex = vertex
    def run(self):
        print "Starting " + self.name
        bfs(self.graphname, self.vertx)
        print "Exiting " + self.name

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

	g = Graph()

	a = open(graph, "r")
	graph = a.read().splitlines()
	a.close()

	for i in range(0,n + 1):
		g.addVertex(i)	

	for line in graph:
		graphu = line.split("\t")
		g.addEdge(int(graphu[0]), int(graphu[1]), 0)


	for v in g:
		if activeCount() == 0:
			thread1 = myThread(g, v)
			#print "%s: " % s
			#print "%s: " % s.getId()
		
			thread1.start()
			thread2.start()
			thread3.start()
			thread4.start()


		#m = bfs(g, s)
		
		
	print longest
		

def bfs(g, s):
	
	global longest	
	
	s.dist = 0
	maxdist = 0
	
	Q = Queue.Queue(maxsize=0)
	Q.put(s)
	
	while not Q.empty():
		u = Q.get()
		for e in u.getConnections():
			if e.dist > 999999999:
				#sys.stdout.write(" %s" % e.getId())
				Q.put(e)
				e.dist = u.dist + 1
				if e.dist > maxdist:
					maxdist = e.dist
				#sys.stdout.write(" %s:" % e.getId())
				#sys.stdout.write("%s" % e.dist)
		#print " "
	for a in g:
		a.dist = 1000000000
			
	if maxdist > longest:
		longest = maxdist




		
MakeRGraph("soc-Slashdot0811.txt", 77360)
#MakeRGraph("test.txt", 7)
#MakeRGraph("test1.txt", 11)








