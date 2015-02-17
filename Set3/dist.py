import random

def getrand100():
 a=random.randint(10**(99),(10**100)-1)
 return a


def modexp(x,y,N):
 if y == 0:
  return 1
 z=modexp(x,(y/2),N)
 if (y%2) == 0:
  return ((z**2) % N)
 else:
  return ((x*z**2)%N)


def isprime(N):
 a=random.randint(2, (N-1))
 if ( modexp(a, N-1, N)  == 1):
  return True
 return False


def nextprime(i):
 
 if (i%2) == 0:
  i+=-1

 a=False

 while(a == False):
  i+=2
  for j in range(0,51):
   a=isprime(i)
 return i
  

def avgdist():
 a=0
 b= [0]*1001
 d=0
 acc=0
 while (a<=1000):
  s=getrand100()
  print s
  b[a]=nextprime(s)-s
  a+=1
 
 while (d<=1000):
  acc+=b[d]
  d+=1
 
 e=acc/10
 print "The average distance is", e

avgdist()


