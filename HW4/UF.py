# Unlike in Java, not all Python classes were originally descendants of a
# single 'object' class.  To make inheritance work well, it is convenient
# to impose this.  The following line declares UF to be a class, and
# a child of the 'object class:
class UF(object):

  ''' The elements to be unioned together are numbered 0 through n-1.  Each
      identifier for a union-find class is also an integer from 0 through
      n-1.

      _id[i] tells I.D. number of union-find class i is in
      _l[j] tells the list of elements for class with identifier j, or None 
      if there is currently no class with that identifier.
      
      When two classes are merged, the new class assumes
      the identifier of the larger of the old classes.  
      
      Suppose two classes of the same size are merged through a call to
      union(i1,i2).  Then the new class takes on the I.D. number
      of the old class that contained the first parameter, i1.
      (This rule is of no consequence for the correctness, but
      it makes it easier to grade if everybody adopts it.)
   '''


  # Get number of elements in the collection of union-find classes
  def getn(self):
    return len(self._l)

  # Initialize a union-find structure with elements {0, 1, ... n-1}, each
  #  initially in its own union-find class
  def __init__(self, n):
    self._id = list(range(n))
    self._l = [[i] for i in range(n)]

  # String representing current state of union-find structure.  Use is similar
  #  to that of toString() in Java.
  def __str__(self):
     return ''.join(['id:     ', str(self._id), '\nl:      ',  str(self._l)]) 

  # Find I.D. number of union-find class that currently contains element i
  def find(self, i):
    return self._id[i]

  # Return a reference to the list of members of the class containing i.
  def classOf (self, i):
     return self._l[self.find(i)]

  # Check whether i and j are currently in the same union-find class.  If
  #  so, return False.  Otherwise, merge the union-find classes containing
  #  i and j and return True.
  def union(self, i, j):
    if self.find(i) == self.find(j):
        return False

    left = self.classOf(i);
    right = self.classOf(j);
 
    if right == None or left == None:
        return False

    if len(left) < len(right):        
        right.extend(left)
        self._l[self.find(j)] = right
        self._l[i] = None
        self._id[i] = self.find(j)
    else:
        left.extend(right)
        self._l[self.find(i)] = left
        self._l[j] = None
        self._id[j] = self.find(i)

    return True



