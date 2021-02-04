from time import time
from math import sqrt

start = time()

n = 2000000
top = int( sqrt( n))

num = list( iter( range( n)))

num[ 1] = 0

for i in range(2, top):
    p = num[ i]
    if p > 0:
        for j in range( p * p, n, p):
            num[ j] = 0

print( sum( num))

print( "time: ", time() - start)



