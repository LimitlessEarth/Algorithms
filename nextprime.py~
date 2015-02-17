import random

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
  

 print "Next prime is ", i
 return i

nextprime(2013**50)

