import sys
import random

a=2
N=1
b=0

while(b==0) :
 print "N=", N

 if (2**(N-1)) % N == 1:
  for c in range(2, N):
   if (N % c) == 0:
    print "PSO 2", N
    

    if (3**(N-1)) % N == 1:
     for c in range(2, N):
      if (N % c) == 0:
       print "PSO 3", N
       

       if (2013**(N-1)) % N == 1:
        for c in range(2, N):
         if (N % c) == 0:
          print "PSO 2013", N
          b=1
          
 N=N+1

