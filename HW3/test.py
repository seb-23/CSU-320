import sys, os

def main():
	print("Hello world")
	print(sys.argv[0])
	print(sys.argv[1])

if __name__ == "__main__":
    main()




'''
def MWISMemoizedAux(L, i, DPTable):
	if i == 0:
		return 0

	#if L[i][PREVIOUS] != 0:
		#j = L[i][PREVIOUS]
		#DPTable[len(L)-i] = L[i][WEIGHT] + L[j][WEIGHT]
		#DPTable[i] = max(L[i][WEIGHT] + MWISMemoizedAux(L, j, DPTable), MWISMemoizedAux(L, i-1, DPTable))
		#print(DPTable)
		#return max(L[i][WEIGHT] + MWISMemoizedAux(L, j, DPTable), MWISMemoizedAux(L, i-1, DPTable))
		#return 
	
	DPTable[len(L)-i] = max(L[len(L)-i][WEIGHT] + DPTable[L[len(L)-i][PREVIOUS]], DPTable[len(L)-i-1]) #last index should be 8
	
	
	#print(DPTable)
	#return max(L[i][WEIGHT], MWISMemoizedAux(L, i-1, DPTable))
	
	j = L[i][PREVIOUS]
	return max(L[i][WEIGHT] + MWISMemoizedAux(L, j, DPTable), MWISMemoizedAux(L, i-1, DPTable))


'''


'''
	if i == 0:
		return 0
		
	if L[i][PREVIOUS] != 0:
		j = L[i][PREVIOUS]
		return max(L[i][WEIGHT] + MWISExponential(L, j), MWISExponential(L, i-1))  # GOTTA FIX THIS
	
	return max(L[i][WEIGHT], MWISExponential(L, i-1))

'''

'''
the method is reconstruct()

	if len(L) - i == 1:
		DPTable[len(L)-i] = L[len(L)-i][WEIGHT]
		return max(L[i][WEIGHT], reconstruct(L, i-1, DPTable))
	
	if L[i][PREVIOUS] != 0:
		DPTable[len(L)-i] = max(L[len(L)-i][WEIGHT] + DPTable[L[len(L)-i][PREVIOUS]], DPTable[len(L)-i-1])
		j = L[i][PREVIOUS]
		return max(L[i][WEIGHT] + reconstruct(L, j, DPTable), reconstruct(L, i-1, DPTable))
	
	DPTable[len(L)-i] = max(L[len(L)-i][WEIGHT] + DPTable[L[len(L)-i][PREVIOUS]], DPTable[len(L)-i-1])
	#DPTable[len(L)-i] = max(L[len(L)-i][WEIGHT], DPTable[len(L)-i-1])
	
	return max(L[i][WEIGHT], reconstruct(L, i-1, DPTable))

'''


'''

def closestAux(X, Y):
	best = 0.0
	bestPair = []
	
	if len(X) == len(Y):
		fx = X[:len(X)//2]
		#fy = sorted(fx, key = lambda yy: (yy[1]))
		sx = X[len(X)//2:]
		#sy = sorted(sx, key = lambda yyy: (yyy[1]))
		#return min(closestAux(fx,Y), closestAux(sx,Y))
		one, pairf = closestAux(fx,Y)
		best, bestPair = closestAux(sx,Y)
		#or
		one, pair = brute(fx)
		best, bestPair = brute(sx)
		
		if best > one:
			best = one
			bestPair = pair

	for i in range(len(X)-1):
		for j in range(i+1, len(X)):
			distance = distsq(X[i], X[j])
			if distance < best:
				best = distance
				bestPair = [X[i], X[j]]

	
	midway = (sx[len(sx)-1][0] - fx[len(fx)-1][0]) + fx[len(fx)-1][0]
	left = midway - best
	right = midway + best
	
	strip = []
	i = len(fx)-1
	while fx[i][0] > left:
		strip.append(fx[i])
		i -= 1 
		
	j = len(sx)-1
	while sx[j][0] < right:
		strip.append(sx[j])
		j -= 1 
		
'''	
		
		
		
'''

	best = 0.0
	bestPair = []
	fx = X[:len(X)//2]
	sx = X[len(X)//2:]
	
	for i in range(len(fx)-1):
		for j in range(i+1, len(fx)):
			distance = distsq(fx[i], fx[j])
			if distance < best:
				best = distance
				bestPair = [fx[i], fx[j]]
	
	for i in range(len(fy)-1):
		for j in range(i+1, len(fy)):
			distance = distsq(fy[i], fy[j])
			if distance < best:
				best = distance
				bestPair = [fy[i], fy[j]]
	
	midway = (sx[len(sx)-1][0] - fx[len(fx)-1][0]) + fx[len(fx)-1][0]
	left = midway - best
	right = midway + best
	
	strip = []
	i = len(fx)-1
	while fx[i][0] > left:
		strip.append(fx[i])
		i -= 1 
		
	j = len(sx)-1
	while sx[j][0] < right:
		strip.append(sx[j])
		j -= 1 
	
	
	
	#fy = Y[:len(Y)//2]
	#sy = Y[len(Y)//2:]
	
	#min(closestAux(fx,Y), closestAux(sx,Y))

	return 0.0, [(0.0,0.0),(0.0,0.0)] 
      
      
'''
	
	
'''

MY CODE BEFORE the base case recursive call to brute(S)


	one = X[:len(X)//2]
	#uno = sorted(one, key = lambda s: (s[1]))
	two = X[len(X)//2:]
	#dos = sorted(two, key = lambda c: (c[1]))
	b, pair = brute(one)
	best, bestPair = brute(two)
	
	if best > b:
		best = b
		bestPair = pair
	
	midway = (two[len(two)-1][0] - one[len(one)-1][0]) + one[len(one)-1][0]
	left = midway - best
	right = midway + best
	
	strip = []
	i = len(one)-1
	while one[i][0] > left:
		strip.insert(0, one[i])
		i -= 1 
		
	j = 0
	while two[j][0] < right:
		strip.append(two[j])
		j += 1 
		
	strip = sorted(strip, key = lambda s: (s[1]))
	
'''



'''

TODAY:

	best = 0.0
	bestPair = []
	
	if len(X) <= 3:
		return brute(X)
		
	one = X[:len(X)//2]
	#uno = Y[:len(Y)//2]
	#uno = sorted(one, key = lambda s: (s[1]))
	two = X[len(X)//2:]
	#dos = Y[len(Y)//2:]
	#dos = sorted(two, key = lambda c: (c[1]))
		
	#b, pair = closestAux(one, uno)
	#b, pair = closestAux(one, Y)
	#best, bestPair = closestAux(two, dos)
	best, bestPair = min(closestAux(one, Y), closestAux(two, Y))
	
	#if best > b:
		#best = b
		#bestPair = pair
	
	#midway = two[0]

	midway = (two[0][0] - one[len(one)-1][0]) + one[len(one)-1][0]
	
'''
