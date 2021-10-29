'''
Given a set of intervals on the real line is an *independent set* if no 
pair of the intervals intersects.  

Problem:  Given a set X of intervals on the real line, each with a weight,
find an independent subset of X of maximum total weight.

For simplicity, we will assume that the coordinates of the endpoints of the 
intervals and the weights are all positive integers and that the left 
endpoint of each interval is strictly less than the right endpoint of an 
interval.

Example input file:
1,4,2  
2,6,4
5,7,4
3,10,7
8,11,2
9,12,1

This is a set of six intervals.  The first interval's left endpoint 
is at 1, its right endpoint is at 4 and it has a weight of 2.
The second interval's left endpoint is at 2, its right endpoint is
at 7 and its weight is 4, etc. 

A solution to this instance is [(1, 4, 2), (5, 7, 4), (8, 11, 2)].  No 
two of these intervals intersect (it is an independent set) and their total 
weight is 2+4+2 = 8.  
'''
    
BEGIN = 0
END = 1
WEIGHT = 2
PREVIOUS = 3

'''
Read the interval in from a file, where each line consists of the sequence
of four non-negative integers, separated by spaces.
The first three integers are the beginning point,
the ending point, and the weight of the interval.  The last element is 
reserved for information explained below.  The returned list is sorted
in ascending order of right endpoint.

Example six-line input file:

2 6 4
8 11 2
5 7 4
1 4 2
3 10 7
9 12 1
'''
def readIntervals(filename):
   fp = open(filename, 'r')
   L = [[0,0,0,0]] + [[int(x) for x in line.split()] + [0] for line in fp]
   # Return the four-tuples in ascending order of right endpoint.  See
   # the Python tutorial for use of lambda functions.  You may find
   # it helpful when you write assignPrevs.
   return (sorted(L, key = lambda fourTuple: fourTuple[END]))

'''
IntvlList is a list of the intervals in ascending order of endpoint.
Each interval is a four-tuple.  The first three elements are the
beginning point, the endpoint, and the weight of the interval.
The fourth element of each interval I is filled in by this procedure,
and gives index of the last interval J in IntvlList whose right endpoint
precedes the left endpoint of interval I, or 0 of there is no such interval.

It is easy to come up with an O(n^2) algorithm for this problem.
For full credit, you must use an O(n log n) algorithm.
'''
'''
def assignPrevs(IntvlList):
	total = 0
	for i in range(2, len(IntvlList)):
		j = 1
		while i > j:
			total += 1
			if IntvlList[i][BEGIN] - IntvlList[j][END] >= 1:
				IntvlList[i][PREVIOUS] = j
				
			j += 1
	print("Total:", total)
	return IntvlList
'''
def assignPrevs(IntvlList):
	for i in range(2, len(IntvlList)):
		j = i - 1
		while j > 0:
			if IntvlList[i][BEGIN] - IntvlList[j][END] >= 1:
				IntvlList[i][PREVIOUS] = j
				break
				
			j -= 1

	return IntvlList

'''
Find a maximum-weight independent set among a set of weighted intervals.
L is a list of intervals, sorted in ascending order of right endpoint.
The initial element of the list is a dummy; the indices of the given
intervals start at 1.  

Each interval I is a four-tuple:
I[0] is the beginning point, a positive integer.
I[1] is the ending point, a positive integer.
I[2] is the weight, a positive integer.
I[3] is the index in L of the last interval J in L whose right endpoint comes
before the beginning point I[0] of I, or 0 if there is no such interval.

The method returns the weight of a maximum-weight independent subset of
intervals in L[1..i], that is, a maximum-weight subset such that no pair of 
intervals in the subset intersects.  A precondition on i is that 
0 <= i < len(L).  If i = 0, then L[1..0] is empty and it returns 0.

Otherwise, the strategy is a recursive approach that works by induction on i
and does not use dynamic programming or memoization.  It considers two
possibilities:  the maximum independent set either doesn't contain L[i]
or it does.  It uses recursive calls to find the maximum weight
of any independent set that contains L[i] and the maximum weight
of any independent set that does not contain L[i].  It returns the
maximum of these two weights.
'''
'''
def MWISExponential(L, i):
	if i == 0:
		return 0

	if L[i][PREVIOUS] != 0:
		j = L[i][PREVIOUS]
		return max(L[i][WEIGHT] + MWISExponential(L, j), MWISExponential(L, i-1))
	
	return max(L[i][WEIGHT], MWISExponential(L, i-1))
	'''
'''
def MWISExponential(L, i):
	if i == 0:
		return 0

	if L[i][PREVIOUS] != 0:
		j = L[i][PREVIOUS]
		return max(L[i][WEIGHT] + MWISExponential(L, j), MWISExponential(L, i-1))
	
	return max(L[i][WEIGHT], MWISExponential(L, i-1))
	'''
	
'''
def MWISExponential(L, i):
	if i == 0:
		return 0
	q = -1
	for j in range(1, i+1):
		newq = L[j][WEIGHT] +  MWISExponential(L, i-j)
		if newq > q:
			q = newq
	#return max(L[i][WEIGHT],MWISExponential(L, i-1))
	return q
'''

'''
def MWISExponential(L, i):
	if i == 0:
		return 0
	q = -1
	for j in range(1, i+1):
		MWISExponential(L, i-j)
		newq = L[j][WEIGHT] + MWISExponential(L, L[j][PREVIOUS])
		if newq > q:
			q = newq
	#return max(L[i][WEIGHT],MWISExponential(L, i-1))
	return q
'''	
	
def MWISExponential(L, i):
	if i == 0:
		return 0
		
	total = 0
	j = L[i][WEIGHT] + L[i][PREVIOUS]
	while j > 0:
		total += L[j][WEIGHT]
		tmp = L[j][PREVIOUS]
		j = tmp
		
	return max(total, MWISExponential(L, i-1))


'''
Front end for MWISMemoizedAux.  It needs to create an empty dynamic programming
table, make a call to MWISMemoizedAux to fill it in, then call reconstruct
to reconstruct a maximum-weight independent set from the table, and return
it.
'''
def MWISMemoized(IntvlList):
	DPTable = [0]*len(IntvlList)
	MWISMemoizedAux(IntvlList, len(L)-1, DPTable)
	reconstruct(IntvlList, len(L)-1, DPTable)
	return DPTable

'''
Memoized version of MWISExponential.  A front-end (below), creates
an empty dynamic programming table, DPTable, in advance of the first
call.  DPTable[i] is to contain the maximum weight of any independent
subset of L[1..i].  This procedure fills out the table by memoization.
In addition to this, it returns the maximum weight of an independent
set on L[1..i] (or 0 if i = 0).
'''
'''
def MWISMemoizedAux(L, i, DPTable):
	print("HI")
	if i == 0:
		return 0
	
	DPTable[len(L)-i] = max(L[len(L)-i][WEIGHT] + DPTable[L[len(L)-i][PREVIOUS]], DPTable[len(L)-i-1])
	
	j = L[i][PREVIOUS]
	return max(L[i][WEIGHT] + MWISMemoizedAux(L, j, DPTable), MWISMemoizedAux(L, i-1, DPTable))
	
				c = 0
			e = L[len(L)-i][PREVIOUS]
			while e > 0:
				c += L[e][WEIGHT]
				tmp = L[e][PREVIOUS]
				e = tmp
	
'''
'''
def MWISMemoizedAux(L, i, DPTable):
	if i == 0:
		return 0
		
	if len(L) - i == 1:
		DPTable[len(L)-i] = L[len(L)-i][WEIGHT]
		return max(L[i][WEIGHT], MWISMemoizedAux(L, i-1, DPTable))
		
	if L[i][PREVIOUS] != 0:
		if DPTable[len(L)-i-1] != DPTable[len(L)-i-2]:
			DPTable[len(L)-i] = max(L[len(L)-i][WEIGHT] + DPTable[L[len(L)-i][PREVIOUS]], DPTable[len(L)-i-1])
		else:
			c = 0
			e = L[len(L)-i][PREVIOUS]
			while e > 0:
				c += L[e][WEIGHT]
				tmp = L[e][PREVIOUS]
				e = tmp
			DPTable[len(L)-i] = max(L[len(L)-i][WEIGHT] + c, DPTable[len(L)-i-1])
			print(c, DPTable)
		j = L[i][PREVIOUS]
		return max(L[i][WEIGHT] + MWISMemoizedAux(L, j, DPTable), MWISMemoizedAux(L, i-1, DPTable))
	
	DPTable[len(L)-i] = max(L[len(L)-i][WEIGHT], DPTable[len(L)-i-1])
	return max(L[i][WEIGHT], MWISMemoizedAux(L, i-1, DPTable))
'''
'''
def MWISMemoizedAux(L, i, DPTable):
	if i == 0:
		return 0
		
	if len(L) - i == 1:
		DPTable[len(L)-i] = L[len(L)-i][WEIGHT]
		return max(L[i][WEIGHT], MWISMemoizedAux(L, i-1, DPTable))
		
	if L[i][PREVIOUS] != 0:
		if DPTable[len(L)-i-1] != DPTable[len(L)-i-2]:
			DPTable[len(L)-i] = max(L[len(L)-i][WEIGHT] + DPTable[L[len(L)-i][PREVIOUS]], DPTable[len(L)-i-1])
		else:
			DPTable[len(L)-i] = max(L[len(L)-i][WEIGHT] + c, DPTable[len(L)-i-1])
		j = L[i][PREVIOUS]
		return max(L[i][WEIGHT] + MWISMemoizedAux(L, j, DPTable), MWISMemoizedAux(L, i-1, DPTable))
	
	DPTable[len(L)-i] = max(L[len(L)-i][WEIGHT], DPTable[len(L)-i-1])
	return max(L[i][WEIGHT], MWISMemoizedAux(L, i-1, DPTable))

'''

'''
def MWISMemoizedAux(L, i, DPTable):
	#print("HI")
	if i == 0:
		return 0
		
	if len(L) - i == 1:
		DPTable[len(L)-i] = L[len(L)-i][WEIGHT]
		return max(L[i][WEIGHT], MWISMemoizedAux(L, i-1, DPTable))
		
	if L[i][PREVIOUS] != 0:
		DPTable[len(L)-i] = L[len(L)-i][WEIGHT] + DPTable[L[len(L)-i][PREVIOUS]]
		j = L[i][PREVIOUS]
		return max(L[i][WEIGHT] + MWISMemoizedAux(L, j, DPTable), MWISMemoizedAux(L, i-1, DPTable))
	
	DPTable[len(L)-i] = L[len(L)-i][WEIGHT]+ DPTable[L[len(L)-i][PREVIOUS]]
	return max(L[i][WEIGHT], MWISMemoizedAux(L, i-1, DPTable))
'''
def MWISMemoizedAux(L, i, DPTable):
	if i == 0:
		return 0
	elif DPTable[i] > 0:
		return DPTable[i]
	else:
		j = L[i][PREVIOUS]
		if j > 0:
			DPTable[i] = L[i][WEIGHT] + MWISMemoizedAux(L,j,DPTable)
			MWISMemoizedAux(L,i-1,DPTable)
		else:
			DPTable[i] = L[i][WEIGHT]
			MWISMemoizedAux(L,i-1,DPTable)
		if DPTable[i] > 0 and i == len(DPTable)-1:
			for c in range(1, len(DPTable)-1):
				if DPTable[c] > DPTable[c+1]:
					DPTable[c+1] = DPTable[c]
					
			return MWISMemoizedAux(L,0,DPTable)
		return DPTable[i]
		
		'''	
		
					#while j > 0:
			#k = j
			v = L[i][WEIGHT] + MWISMemoizedAux(L,j,DPTable)
			#j = L[k][PREVIOUS]
		
		
	else:
		q = -1
		for j in range(1,i+1):
			newq = L[i][WEIGHT] + MWISMemoizedAux(L,i-j,DPTable)
			if newq > q:
				q = newq
			DPTable[i] = q
	'''		

'''
def MWISMemoizedAux(L, i, DPTable):
	if i == 0:
		return 0
		
	if i == 1:
		DPTable[i] = L[i][WEIGHT]
		return max(L[i][WEIGHT], MWISMemoizedAux(L, i-1, DPTable))
		
	if L[i][PREVIOUS] != 0 and DPTable[i] == 0:
		j = L[i][PREVIOUS]
		DPTable[i] = max(L[i][WEIGHT] + MWISMemoizedAux(L, j, DPTable), MWISMemoizedAux(L, i-1, DPTable))
		return DPTable[i]
		
	if DPTable[i] == 0:
		DPTable[i] = max(L[i][WEIGHT], MWISMemoizedAux(L, i-1, DPTable))
		return DPTable[i]
		
	if L[i][PREVIOUS] != 0:
		j = L[i][PREVIOUS]
		DPTable[i] = max(L[i][WEIGHT] + MWISMemoizedAux(L, j, DPTable), MWISMemoizedAux(L, i-1, DPTable))
		return DPTable[i]
	
	DPTable[i] = max(L[i][WEIGHT], MWISMemoizedAux(L, i-1, DPTable))
	return DPTable[i]

'''
'''
def MWISMemoizedAux(L, i, DPTable):
	if i == 0:
		return 0
		
	if L[i][PREVIOUS] != 0:
		j = L[i][PREVIOUS]
		DPTable[i] = max(L[i][WEIGHT] + MWISMemoizedAux(L, j, DPTable), MWISMemoizedAux(L, i-1, DPTable))
		return DPTable[i]
	
	DPTable[i] = L[i][WEIGHT]
	MWISMemoizedAux(L, i-1, DPTable)
	return DPTable[i]
'''	

		
	
'''
Recursively reconstruct the maximum-weight set of intervals from L[1..i].
If i == 0, this list is empty.  The strategy is similar to the strategies
of other algorithms we have studied for reconstructing a solution from
a dynamic programming table.

Reconstruct should return the set of intervals that are in the maximum-weight subset.
'''
def reconstruct(L, i, DPTable):
	if i == 0:
		DPTable.pop(0)
		return 0

	if DPTable[i] == DPTable[i-1] and DPTable[i-1] == DPTable[len(DPTable)-1]:
		DPTable.pop()
		return reconstruct(L, i - 1, DPTable)
		
	DPTable[i] = [L[i][BEGIN], L[i][END], L[i][WEIGHT]]
	p = L[i][PREVIOUS]
	
	while i - p > 1:
		DPTable.pop(i-1)
		i -= 1
	
	return reconstruct(L, p, DPTable)

'''
Front end for MWISDPAux.  It creates the dynamic programming table before
calling MWISDPAux to get a filled-in dynamic programming table, then
calls reconstruct to reconstruct a maximum independent set of intervals
in L, and returns this set as a list of tuples, where each tuple
is the beginning point, ending point and weight of an interval.
'''
def MWISDP(IntvlList):
	assignPrevs(IntvlList)
	DPTable = []
	max_intervals = []
	DPTable = MWISDPAux(IntvlList)
	reconstruct(IntvlList, len(IntvlList)-1, DPTable)
	return DPTable

'''
Implement a bottom-up algorithm to fill in the dynamic programming table for 
L[1..len(L)-1].  The method should create the table and return it.
'''
def MWISDPAux(L):
	DPTable = [0]*len(L)
	assignPrevs(L)
	for i in range(1, len(L)):
		if DPTable[i-1] != DPTable[i-2]:
			DPTable[i] = max(L[i][WEIGHT] + DPTable[L[i][PREVIOUS]], DPTable[i-1])
		else:
			total = 0
			pre = L[i][PREVIOUS]
			while pre > 0:
				total += L[pre][WEIGHT]
				tmp = L[pre][PREVIOUS]
				pre = tmp
			DPTable[i] = max(L[i][WEIGHT] + total, DPTable[i-1])
	return DPTable

if __name__ == '__main__':
    L = readIntervals('WI1.txt')
    print()
    print("Original:")
    print(L)
    print()
    print("AssignPrevs:")
    assignPrevs(L)
    print(L)
    print()
    best = MWISExponential(L, len(L)-1)
    print ('Returned by MWISExponential ', best)
    DPTable = [0]*len(L)
    MWISMemoizedAux(L, len(L)-1, DPTable)
    print ('DP Table after MWISMemoizedAux(L, len(L)-1, DPTable): ', 
            DPTable)
    print ('Returned by MWISMemoized: ', MWISMemoized(L))
    print ('Returned by MWISDPAux: ', MWISDPAux(L))
    print ('Results returned by MWISDP: ', MWISDP(L))
