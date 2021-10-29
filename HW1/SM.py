def readSMFile(filename):
    MPrefLists = [[]]
    WPrefLists = [[]]
    with open(filename) as f:
        Lines = f.readlines()
        instanceSize = int(Lines[0][:-1])
        for i in range(instanceSize):
            New_list = [0] + [int(elem) for elem in str(Lines[i+1][:-1]).split(" ")]
            MPrefLists.append(New_list)
        for i in range(instanceSize+1,2*instanceSize+1,1):
            New_list = [0] + [int(elem) for elem in str(Lines[i+1][:-1]).split(" ")]
            WPrefLists.append(New_list)
    return instanceSize, MPrefLists, WPrefLists


def ComputeInvPrefLists(PrefLists):
	# FILL IN CODE HERE
	InvPrefLists = [[]]
    
	for j in range(1,len(PrefLists)):
		
		element = []
		element.append(0)
		
		for i in range(1, len(PrefLists)):
			
			found = PrefLists[j].index(i)
			element.append(found)
			
		InvPrefLists.append(element)
    
	return InvPrefLists



def propose(newMan, woman, InvWomenPrefLists, Fiance, MStartPositions):
	# FILL IN CODE HERE
	i = InvWomenPrefLists[woman][newMan]			# i contains the position of newMan in woman's preference list
	j = InvWomenPrefLists[woman][Fiance[woman]]		# j contains the position of woman's current Fiance (or 0 if not engaged)
    
	if j > i or j == 0:								# if i ranks higher than j then execute...
		reject = Fiance[woman]
		Fiance[woman] = newMan
	
		if j != 0:
			MStartPositions[reject] += 1				# when a man is rejected, increment the rejected man's value in MStartPositions
		
		
		return reject
		
		
	return newMan

def StackOfMen(instanceSize):
    return list(range(1, instanceSize+1))

def GaleShapley(instanceSize, MPrefLists, WPrefLists):
	# FILL IN CODE HERE ...
	galeShapely = []
	MStartPositions = [0]
	Fiance = [0]

	for k in range(0, instanceSize):
		MStartPositions.append(1)
		Fiance.append(0)
		galeShapely.append((0, 0))
 
	w = ComputeInvPrefLists(WPrefLists)

	j = 1
	i = 1
	while i < instanceSize + 1:							
		j = 1
		while j < instanceSize + 1:						
			wife = MPrefLists[i][j]

			if Fiance[wife] != i:											#if man i and wife are already engaged then do not execute
				reject = propose(i, wife, w, Fiance, MStartPositions)
																			#int index = m[reject][wife]	
				if i != reject and reject != 0:	
					j = MStartPositions[reject] - 1
					i = reject
																			#int second = propose(reject, woman+1, Fiance, MStartPositions)
				if reject == 0:
					j = instanceSize
					
			else:
				j = instanceSize
				
			j += 1
			
		i += 1

	n = 1
	while n < instanceSize + 1:
		found = Fiance.index(n)
		galeShapely[n-1] = (found, n)
		n += 1


	return galeShapely

def checkStability(instanceSize, MPrefLists, WPrefLists, Matching):
    for i in range(instanceSize):
        Marriage1 = Matching[i]
        m1 = Marriage1[0]
        w1 = Marriage1[1]


        # m1's and m2's rankings of each other
        m1SpousePosition = InvMenPrefLists[m1][w1]
        w1SpousePosition = InvWomenPrefLists[w1][m1]


        # For each later marriage in the list, Marriage2 ...
        for j in range(i+1,instanceSize):
            Marriage2 = Matching[j]
            m2 = Marriage2[0]
            w2 = Marriage2[1]


            # m2, m2's rankings of each other
            m2SpousePosition = InvMenPrefLists[m2][w2]
            w2SpousePosition = InvWomenPrefLists[w2][m2]


            # If m1, w2 prefer each other to their spouses ...
            if m1SpousePosition > InvMenPrefLists[m1][w2] and w2SpousePosition > InvWomenPrefLists[w2][m1]:
                return False, Marriage1, Marriage2 


            # If m2, w1 prefer each other to their spouses ...
            if m2SpousePosition > InvMenPrefLists[m2][w1] and w1SpousePosition > InvWomenPrefLists[w1][m2]:
                return False, Marriage2, Marriage1


    #  If no instabilities have been discovered ...
    return True, (0,0), (0,0)



