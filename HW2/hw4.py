'''
This is an implementation of the adjacency-list representation of a graph
where the vertices are numbered from 0 through n-1.

The class has integer variables recording the number of vertices, n,
and number of edges, m.  The graph has a variable _m that tells the
number of edges.  It has a list _Verts, where _Verts[i] is a list
of neighbors of vertex i.  The number of vertices can be computed
from the length of _Verts.

For example, if _Verts is [[1,2], [], [0]], then there are three
vertices, since there are three lists in it.  Vertex 0
has neighbors 1 and 2, vertex 1 has no neighbors, and vertex 2 has 0 as
its only neighbor.

The first half of the class consists of given files, and the second half
consists of functions for you to implement.

The function for reading a graph from a txt file is at the bottom of this file.
'''

class Graph(object):

  # return number of vertices
  def getn(self):
      return len(self._Verts)

  # return number of edges
  def getm(self):
      return self._m

  # return a copy of the list of neighbors of vertex i
  def neighbors(self, i):
	  return list(self._Verts[i])

  # return a list of ordered pairs giving the edges of the graph
  def getEdges(self):
      EdgeList = []
      for i in range(self.getn()):
          for j in self.neighbors(i):
              EdgeList.append((i,j))
      return EdgeList

  ''' Constructor.  __init__ is a reserved keyword identifying it
      as a constructor.  numVerts tells how many vertices the graph should have.
      EdgeList is a list of ordered pairs, one for each edge, in any order.
      Example: numVerts = 3 and EdgeList = [(0,1), (1,2), (0,2), (2,0)]
  '''
  def __init__ (self, numVerts, EdgeList):
      self._m = len(EdgeList)
      self._Verts = [[] for i in range(numVerts)]
      for u, v in EdgeList:
          self._Verts[u].append(v)

  # add an edge from tail to head.  Does not check for duplicate edges
  def addEdge(self, tail, head):
      self._Verts[tail].append(head)
      self._m += 1

  ''' String representation of the graph.  If G is an instance of the class,
      this is called with str(G).  It is called implicitly when a string
      is expected, e.g. in a call to print(G)
  '''
  def __str__(self):
      return 'n = ' + str(self.getn()) + ' m = ' + str(self.getm()) + '\n' + str(self._Verts)
      
  '''
  Version of dfs that labels each vertex with its parent in the dfs forest, or
  -1 if it is the root of one of the trees in the forest.  In the main
  call of dfs, the loop traverses the vertices in ascending order,
  unless a list of vertices in another order is supplied.

  (You can assign labels to vertices with an array L, where L[i] gives the
  label of vertex i.)
  '''
  def dfs(self, VertOrder = None):
      if VertOrder == None:
          VertOrder = range(self.getn())
      Colored = [False] * self.getn() #label vertices as uncolored
      Parent = [-1] * self.getn() #vertices start out with no parent
      for j in range(self.getn()):
          if Colored[VertOrder[j]] == False:
              self.dfsVisit(VertOrder[j], Colored, Parent)
      return Parent

  ''' DFSVisit.  Colored[j] = True if vertex j is Colored, and it's False if j is
      white.  The parameter i is the vertex number of the vertex to start
      at, and it must be white.  Parent is a list of parent labels that have
      been assigned so far.
  '''
  def dfsVisit(self, i, Colored, Parent):
      Colored[i] = True
      for j in self.neighbors(i):
          if not Colored[j]:
              Parent[j] = i
              self.dfsVisit(j, Colored, Parent)
      return Parent
      
  ''' Return the transpose of the graph, that is, the result of reversing
      all the edges
  '''
  def transpose(self):
	  # FILL IN CODE HERE IN PLACE OF THE FOLLOWING LINE
	  EdgeList = self.getEdges()
	  Edge = []

	  for i in range(len(EdgeList)):
		  Edge.append([EdgeList[i][1], EdgeList[i][0]])
		
	  GT = Graph(self.getn(), Edge)
	
	  return GT
      
  '''
  This is a version of DFS that assigns discovery and finishing times to
  vertices.  The VertOrder parameter gives the order in which to cycle
  through the vertices in the main loop of DFS.  If none is given,
  they are traversed in ascending order of vertex number.  It should
  return two lists, Discovery and Finish, where Discovery[i] and Finish[i]
  give the discovery and finishing times of vertex i.

  Let an "event" denote the labeling of a vertex with a discovery or
  finishing time.  The discovery or finishing time label gives the number
  of *prior* events that have occurred.  This means that the first discovery
  time is 0, not 1 and that the last finishing time is 2n-1, where n is the
  number of vertices of 'self'.
  '''
  def timestamp(self, VertOrder = None):
	  # FILL IN CODE HERE
	  Discovery = []
	  Finish = []
	  time = 0
      
	  if VertOrder == None:
		  VertOrder = range(self.getn())
	  Discovery = [-1] * self.getn() #label vertices as uncolored
	  Finish = [-1] * self.getn() #vertices start out with no parent
	  for j in range(self.getn()):
		  if Discovery[VertOrder[j]] == -1:
			  self.timestampVisit(VertOrder[j], time, Discovery, Finish)
      
	  return Discovery, Finish

  '''
  Version of dfsVisit to go with timestamp.  The returned value is
  the new total number of events (labeling with discovery/finishing time)
  that have occurred by the end of the run.
  '''
  def timestampVisit(self, i, time, Discovery, Finish):
	  # FILL IN CODE HERE
	  #sell = sorted(self.neighbors(i))
	  sell = self.neighbors(i)
	  #sell.sort()

	  if Discovery[i] == -1:
		  Discovery[i] = time
		  time += 1

	  trans = self.transpose()
	  tran = trans.neighbors(i)
	  
	  counter = 0
	  for j in sell:
		  if Discovery[j] == -1:
			  self.timestampVisit(j, time, Discovery, Finish)
			  counter += 1
		  else:
			  counter += 1
			  
		  if counter == len(sell):
			  if Finish[i] == -1:
				  Finish[i] = time
				  time += 1
				  
				  
				  train = []
				  for c in tran:
					  train.append([c, Discovery[c]])
				  train = sorted(train, key = lambda x: x[1], reverse=True)
				  
				  tr = []
				  for z in range(len(train)):
					  tr.append(train[z][0])
				  
				  for jk in tr:
					  if Discovery[jk] != -1:
						  self.timestampVisit(jk,time,Discovery,Finish)
			  

	  return time

  '''
          figured it out: it starts at 0; 0 points to 1 so we go to index 1. 
          1 points to 4,2,5 so we choose the lowest integer which is 2. We go
          to index 2; 2 points to 3,6 so we choose 3 because 3 is the lowest 
          integer.We go to index 3 which points to 2,7 since 2 has already been 
          discovered that leaves us with 7 we go to index 7 but 7 deosn't point 
          to anything so we finish the times.
          
          go for lowest undiscovered integer
          if all integers are discovered then finish the index
  '''

  def finishOrder(self):
      # FILL IN CODE HERE
      timestamp = self.timestamp()
      Finish = timestamp[1]
      order = sorted(Finish)

      verts = []
      for i in order:
          index = Finish.index(i)
          verts.append(index)
      
      time = []
      time.append(verts)
      time.append(self.dfs())
      return verts, self.dfs()

  def findAncestors(self, Parent, descendant, ancestor):
      # FILL IN CODE HERE
      ancestors = []
      while descendant != ancestor:
          ancestors.append(descendant)
          descendant = Parent[descendant]
      ancestors.append(ancestor)
      return ancestors

  def testTopSort(self, VertOrder, Parent):
      # FILL IN CODE HERE
      VertOrderInverse = [0] * len(VertOrder)
      for i in range(len(VertOrder)):
          VertOrderInverse[VertOrder[i]] = i

      EdgeList = self.getEdges()
      Cycle = []
      for edge in EdgeList:
          if VertOrderInverse[edge[0]] > VertOrderInverse[edge[1]]:
              vertex = edge[0]
              while vertex != Parent[edge[1]]:
                  Cycle.append(vertex)
                  vertex = Parent[vertex]
              Cycle.reverse()
              return False, Cycle

      return True, []

  def isDag(self):
      # FILL IN CODE HERE
      VertOrder, Parent = self.finishOrder()
      VertOrder.reverse()
      Yes, Cycle = self.testTopSort(VertOrder, Parent)
      if not Yes:
          return False, Cycle
      return True

  def cutpoints(self):
      # FILL IN CODE HERE
      VertOrder = range(self.getn())
      Discovery, Finish = self.timestamp()
      Parent = self.dfs()
      Cut = []
      time = []     # time = low
      
      start = Parent.index(-1)
      for i in Parent:
          if i != Parent.index(-1):
              time.append(i)

      # self.cutpointVisit(VertOrder[j], time, Discovery, Parent, Cut)
      self.cutpointVisit(start, time, Discovery, Parent, Cut)

      return Cut
      
  def cutpointVisit(self, i, time, Parent, Discovery, Cut):
      # FILL IN CODE HERE
      for j in self.neighbors(i):
          if not Discovery[j]:
              Parent[j] = i
              Cut.append(j)
              time = 9
              self.cutpointVisit(j, time, Parent, Discovery, Cut)
			  
      return time, 0

  '''
    Prove the root of Gpi is an articulation point of G iff it has
    at least two children.


    v = non-root vertex
    v is an articulation point iff v has a child s s.t. there is no back edge from
    s or any descendant of s to a proper ancestor of v


                { v.d
    v.low = min{
                { w.d : (u,w) is a back edge for some descendant u of v

    Show how to compute v.low for all vertices v E V in O(E) time


    Show how to compute all articulation points in O(E) time

    PAGE: 622 of Textbook

    Steps:
    Do DFS
    Find Discovery Time
    Find the Lowest Discovery Time for each Vertex by taking one back edge
        Have to find a path back to a Vertex that has already been discovered
    (U, V) or (0, 1) U is the parent; V is the child
    L = Lowest Discovery Time
    D = Discovery Time of U
    if L[V] >= D[U]:
        then U is an articulation point
        This is True for all the vertices except Root
    
    FIND A DIFFERENT CONDITION FOR ROOT 
    
  '''
  

def readGraph(filename):
  EdgeList = []
  fp = open(filename, 'r')
  n = int(fp.readline())
  for line in fp:
      u,v  = [int(x) for x in line.split(',')]
      EdgeList.append((u,v))
  fp.close()
  return Graph(n, EdgeList)
  
  '''
  seb
  '''
  
  '''
  	  trans = self.transpose()
	  tran = trans.neighbors(i)
	  train = []
	  for c in tran:
		  train.append(Discovery[c])
  '''
