import time     # for timing executions of your implementations
import math
import random

'''
FORMATTING CONVENTION

The convention for formatting a list of points in this program is to use
a list of lists of pairs of floating-point values.  The first
element in each pair is the x coordinate of a point and the second
is its y coordinate.  There must be at least two points in a list.

Example:  [[3.2,5.8],[4.7,1.2]]
'''

'''
Read a set of points from a file.  
Prconditions:  The file consists of two floating-point values per 
  line, where the first gives the x coordinate of a point and the 
  second gives its y coordinate.  They should be separated by a space.
Postconditions:  the returned list is a list of the points, adhering
  to the formatting convention (above)

Example four-line file:

0.1 0.5
1.0 1.1
5.0 3.5
1.0 4.0

'''
def readPts(filename):
    fp = open(filename)
    return [[float(i) for i in line.split()] for line in fp]


'''
Brute force algorithm for closest pair.

preconditions:  S is a set of points in the plane.
The two returned values are the square of the distance
between the closest pair of points, and a list of two points
adhering to the formatting convention (above), giving the closest
pair.  

This is needed in the closest-pair algorithm for the base case where
 the number of points is two or three.  (Using this as the base case
 prevents us from having to consider what answer to return if there
 is only one point in the list).  Also, allows you to check the
 answers your divide-and-conquer implementation produces.

 Example run:
In [5]: S
Out[5]: [[0.1, 0.5], [1.0, 1.1], [5.0, 3.5], [1.0, 4.0]]

In [6]: brute(S)
Out[6]: (1.1700000000000002, [[0.1, 0.5], [1.0, 1.1]])
'''
def brute(S):
	best = math.inf
	bestPair = []
	
	for i in range(len(S)-1):
		for j in range(i+1,len(S)):
			distance = distsq(S[i], S[j])
			if distance < best:
				best = distance
				bestPair = [S[i], S[j]]
	
	return best, bestPair

'''
Find the closest pair in S

Precondition:  S conforms to the formatting convention, and no two points
  have the same x coordinate
Postcondition:  A tuple has been returned whose first element is the distance 
squared, and whose second element is a list of two points.

This should generate two sorted lists, one sorted by x coordinate
and one sorted by y coordinate, and call closestAux on them.

'''
def closest(S):
	X = sorted(S, key = lambda x: (x[0]))
	Y = sorted(S, key = lambda y: (y[1]))
	best, bestPair = closestAux(X,Y)
	return best, bestPair

'''
preconditions:  X and Y are the same set of points in two-space, no
    two of which share the same x coordinate.
  X is sorted by X coordinate
  Y is sorted by Y coordinate
postconditions:  the returned tuple are the square of the distance of 
  the closest pair and a list of size two giving the closest pair

It should work just like the method 'brute' above, but implement the
O(n log n) divide-and-conquer algorithm we studied.
'''
def closestAux(X, Y):
		
	if len(X) <= 3:
		return brute(X)
		
	one = X[:len(X)//2]
	two = X[len(X)//2:]
	best, bestPair = min(closestAux(one, Y), closestAux(two, Y))
	

	midway = (two[0][0] - one[len(one)-1][0])/2.0 + one[len(one)-1][0]
	left = midway - math.sqrt(best)
	right = midway + math.sqrt(best)
	
	strip = []

	i = len(one)-1
	while one[i][0] >= left:
		strip.insert(0, one[i])
		i -= 1 
		if i < 0:
			break
			

	j = 0
	while two[j][0] <= right:
		strip.append(two[j])
		j += 1 
		if j == len(two):
			break

	strip = sorted(strip, key = lambda s: (s[1]))
	for o in range(len(strip)-1):
		k = o + 1
		while strip[k][1] - strip[o][1] <= math.sqrt(best):
			distance = distsq(strip[o],strip[k])
			if distance < best:
				best = distance
				bestPair = [strip[o], strip[k]]
				
			k += 1
			if k == len(strip):
				break
	
	return best, bestPair
      
'''
Find the square of the distance between two points.
Preconditions:  p1 and p2 are lists of size two floating-point values,
  where the first element in each list is the x coordinate and the second
  is the y coordinate.
Postcondition:  the square of the distance between the two points has
  been returned
'''
def distsq(p1, p2):
	return pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2)

'''
One way to test out the correctness and efficiency of your code is
to uncomment some of the following:
'''
'''
if __name__ == '__main__':
    
    ''' ************************************* '''
    
    S = readPts('points.txt')
    
    print("BRUTUS:", brute(S))
    print("CLOSEST:",closest(S))
    

    size = int(input("Enter number of points:  "))
    print(size)
    A = [[random.random(), random.random()] for i in range(size)]
    
    start = time.perf_counter()
    Soln = closest(A)
    end = time.perf_counter()
    print('\n    Solution for closest: ', Soln)
    print('\n     Elapsed for closest: ', end - start)
    
    start = time.perf_counter()
    Soln = brute(A)
    end = time.perf_counter()
    print('\nSolution for brute-force: ', Soln)
    print('\n Elapsed for brute-force: ', end - start)
    print()
    
    s = int(input("Enter number of points:  "))
    B = [[random.random(), random.random()] for i in range(s)]
    #print("BRUTUS:", brute(B))
    start = time.perf_counter()
    print("CLOSEST:",closest(B))
    end = time.perf_counter()
    print('\n     Elapsed for closest: ', end - start)
'''
