import random

def quicksort(L):
	if len(L) > 1:
		pivot = random.randrange(len(L))
		elements = L[:pivot]+L[pivot+1:]
		left  = [element for element in elements if element < L[pivot]] 
		right =[element for element in elements if element >= L[pivot]]
		return quicksort(left)+[L[pivot]]+quicksort(right)
	return L

def listAlpha(wordlist):
	
	a = open(wordlist,"r")
   	wordlist = a.read().splitlines()
	a.close()
	alphalist = []
	
	for i in range(0,len(wordlist)):
		b = wordlist[i]
		c = list(b)
		d = quicksort(c)
		e = "".join(d)
		alphalist.append(e)

	alphalist.sort()

	seen = set()
	result = []
	for item in alphalist:
		if item not in seen:
			seen.add(item)
			result.append(item)

	f = open("sortedlist.txt", "w")
	for i in range(0, len(result)):
		f.write(result[i] + '\n')
	f.close()
	
		
listAlpha("wordlst.txt")
