import sys
import string
from string import ascii_uppercase
import random
from bisect import bisect_left
import itertools

def quicksort(L):
	if len(L) > 1:
		pivot = random.randrange(len(L))
		elements = L[:pivot]+L[pivot+1:]
		left  = [element for element in elements if element < L[pivot]] 
		right =[element for element in elements if element >= L[pivot]]
		return quicksort(left)+[L[pivot]]+quicksort(right)
	return L


def wordExists(wordlist, word):
    try:
        return wordlist[bisect_left(wordlist, word)].startswith(word,0,len(word))
    except IndexError:
        return False # word_fragment is greater than all entries in wordlist


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

def makeGraphs(sortedlist):

	a = open(sortedlist,"r")
	sortedlist = a.read().splitlines()
	a.close()

	for i in string.uppercase[:26]:
		p = i
		i = Graph()
		# make starting graph for each letter
		addE(i, p, 1, sortedlist)
		currentdfs = dfs(i)
		if currentdfs > gmax:
			gmax = currentdfs

			 
			
def addE(i, p, l, sortedlist):
	a = list(ascii_uppercase)
	while l < 10:
		for j in itertools.combinations(a, l):
			z = list(p)
			o = list(j)
			z = z + o
			x = quicksort(z)
			y = "".join(x)
			print y
			m = wordExists(sortedlist, y)
			if m != False:
				print "WOOO"
				i.addVertex(y)
				i.addEdge(p, y)
		l += 1
	return i
	
		
		


def dfs(g):

	Max = 0	

	for v in iter(g):
		if v.visited == False:
			Current = explore(g, v, 0)
			#sys.stdout.write(" %s" % Current)
			if Current > Max:
				Max = Current
	sys.stdout.write(" %s" % Max)
	return Max

def explore(g, v, Counter):

	v.visited = True
	for e in v.getConnections():
		if e.visited == False:
			return explore(g, e, Counter + 1)

	#sys.stdout.write(" %s" % Counter)
	return Counter
	
				
	
makeGraphs("sl1.txt")
				
		
