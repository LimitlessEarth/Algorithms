import random

def stupid(A):
	b = A + A
	print b
	
	c = open("b.txt", "w")
	c.write(b + '\n')
	c.write(b)
	c.close()

stupid("LALALALALALALA")
