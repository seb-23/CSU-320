'''
  Implements a min priority queue using a binary heap.  It supports the
     following operations in O(log n) amortized time (see comments in
     code below):
       insert()
       extractMin()
       findMin()
       reduceKey()
       len()
     The elements handled by the heap have a heap key and a reference to
       an object of your choosing, giving information about the element.
     The reason the bound is amortized is that when you use {\tt append}
     to append to a Python list and {\tt pop} to pop an element off the list,
     Python periodically resizes the underlying array.  This is an
     expensive operation, but it is O(1) amortized, using the technique
     we talked about in class of doubling the size of the list when
     you need to resize it upward.
'''

class PQ():
    
    class _Item:
        # Constructor for an item that is referenced by an entry in the
        #  heap array (which is implemented with a Python list.  It has a 
        #  heap key, a value, (which can be passed in as an object such as 
        #  a tuple to represent an edge, for example), #  and a position, 
        #  which gives the array index that points to it.
        def __init__(self, k, v, pos):
            self._key = k
            self._value = v
            self._index = pos

        # __lt__ is a reserved keyword.  If you have Item1 and Item2, you
        #  can call it with the statement 'Item1 < Item2'.  It returns True
        #  if the heap key of Item1 is less than that of Item 2.
        def __lt__ (self, other):
            return self._key < other._key

        #  This returns a string that tells what's in the item.  If you
        #   call str() on an item, it returns this string, and if you
        #   call print() on an item, it prints out this string.
        def __str__(self):
            return str(self._key) + ' ' + str(self._value) + ' ' + str(self._index)

    #  Returns true if the parameter is an empty heap.  It can make a call
    #   to the __len__ method given in the public methods.
    def _is_empty(self):
        return len(self) <= 0

    #  Positions are numbered from 0 through n-1 in the array.  This
    #   returns the position of the parent of the element at position j
    def _parentPos(self, j):
        if j == 0:
            return 0
        return int((j-1)/2 + 0.5)

    #  This returns the position of the left child of the element at
    #   position j.  There is no error checking to see if j is beyond
    #   the end of the heap array.
    def _leftChildPos(self, j):
        return (2*j)+1

    #  This returns the position of the right child of the element at 
    #   position j.  Similar to _leftChildPos.
    def _rightChildPos(self, j):
        return (2*j)+2

    #  Return True if the position of the left child position is the position
    #   of an element of the heap array and False if that position is beyond
    #   the end of the heap array.
    def _hasLeftChild(self, j):
        return self._leftChildPos(j) < len(self)

    #  Similar to _hasLeftChild ..
    def _hasRightChild(self, j):
        return self._rightChildPos(j) < len(self)

    #  This swaps the position of the references of two heap items in the
    #    heap array.  It updates the ._index variables in each of these
    #    two objects to reflect the current positions of their references
    #    in the heap array.
    def _swap(self, i, j):
        self._HeapArr[i], self._HeapArr[j] = self._HeapArr[j], self._HeapArr[i]
        self._HeapArr[i]._index = i
        self._HeapArr[j]._index = j


    #  The parameter j is the position of an element that may have a key
    #    that is smaller than that of its parent in a heap where the heap
    #    property is otherwise observed.  It bubbles it upward using calls
    #    to '_swap' to keep the ._index variables of the affected elements
    #    updated.
    def _bubbleUp(self, j):
        if j <= 0 or j >= len(self):
            return 0
        i = self._parentPos(j)
        if self._HeapArr[j] < self._HeapArr[i]:
            self._swap(i,j)
            self._bubbleUp(i)
        pass

    #  This is the heapify of our textbook.   It uses ._swap to perform
    #    the moving of elements to keep the ._index values of the affected
    #    elements updated.
    def _heapify(self, j):
        l = self._leftChildPos(j)
        r = self._rightChildPos(j)
        min = j
        if self._hasLeftChild(j) and self._HeapArr[l] < self._HeapArr[j]:
            min = l

        if self._hasRightChild(j) and self._HeapArr[r] < self._HeapArr[min]:
            min = r

        if min != j:
            self._swap(min,j)
            self._heapify(min)	
        pass

    #  public methods ------------------

    # __len__ is a reserved keyword.  If you have a heap P, you can call it with
    #    len(P); it will tell how many items are currently in P.
    def __len__(self):
        return len(self._HeapArr)

    #  Constructor:  creates an empty heap.  The only actual data in the heap
    #   is an array of references to elements of type self._Item that were
    #   created during calls to self.insert().
    def __init__(self):
        self._HeapArr = []


    #  Returns a string that displays the contents of the heap.  This
    #   is called with 'str()' or 'print()', and in other contexts where
    #   the heap is supposed to be treated as a string.
    def __str__(self):
        if len(self) == 0:  
             return ""
        else:  
             return self.strAux(0, 0, '')

    def strAux(self, pos, depth, outString):
        s = ''
        for Item in self._HeapArr:
            s += '\n' + str(Item)
        return s
        

    '''
    # Alternative display for heap, using indentation to indicate
    #  depth in the tree.
    def strAux(self, pos, depth, outString):
        print(pos)
        outString = outString + '\n' + ' ' * depth + str(self._HeapArr[pos])
        print(outString)
        if self._hasLeftChild(pos):
            outstring = self.strAux(self._leftChildPos(pos), depth+1, outString)
        if self._hasRightChild(pos):
            outstring = self.strAux(self._rightChildPos(pos), depth+1, outString)
        print(outString)
        return outString
    '''

    #  Insert a new element in the heap, returning the element Item of type 
    #   self._Item (see above) that gets created for its heap entry to point to.
    #   This is so you can insert Item to an array or dictionary, and its
    #   ._index variable will be updated whenever ._swap it called.  (Swap
    #   moves the position of the reference to it in the array, but it does 
    #   not move the address of the Item, so a pointer to it in an array
    #   or dictionary is stable even when a reference to it is being moved 
    #   around the heap array.
    def insert(self, key, value):
        token = self._Item(key, value, len(self._HeapArr))
        self._HeapArr.append(token)
        self._bubbleUp(len(self._HeapArr) - 1)
        return token

    #  Reduce the key of an element represented by Item, which is of type
    #   self._Item (see above).  Initially, the references obey the heap
    #   property.  After reducing the key, swap references around in the heap
    #   array so that the references once again obey the heap property.
    def reduceKey(self, Item, newkey):
        Item._key = newkey
        i = Item._index
        if Item._index < len(self)-1:
            self._heapify(Item._index)
        if Item._index > 0 and Item._index == i:
            self._bubbleUp(Item._index)
        pass

    #  Return information about the min element in the heap without
    #    removing it from the heap.  Return None if it is empty
    def findMin(self):
        if self._is_empty():
            return None
        item = self._HeapArr[0]
        return (item._key, item._value)

    #  Extract the reference to an element of the heap that has a minimum key, 
    #   then swap references around so that the heap property is restored.
    #   Similar to Heap-Increase-Key in our book chapter, which describes
    #   how to do the same thing on a max heap.  The returned values should
    #   be just like the ones that are returned by a call to findMin().
    def extractMin(self):
        item = self._HeapArr[0]
        self._swap(0,len(self)-1)
        self._HeapArr.pop(len(self)-1)
        self._heapify(0)

        i = len(self)-1
        while i > 1 and self._HeapArr[self._parentPos(i)] > self._HeapArr[i]:
            self._swap(self._parentPos(i), i)
            i = self._parentPos(i)
		
        return (item._key, item._value)

if __name__ == '__main__':
    P = PQ()
    Items = [None] * 5
    Items[0] = P.insert(8,'blue')
    Items[1] = P.insert(10,'red')
    Items[2] = P.insert(6,'yellow')
    Items[3] = P.insert(9,'green')
    Items[4] = P.insert(7,'orange')
    print ('Initial Items array, for looking up a heap element in O(1) time: ')
    print ('The first element of each entry is the current key of each element.')
    print ('\n The second element is satellite information about the element')
    print ('  which is a string giving a color in this example.  It can be')
    print ('  any kind of object.')

    print ('\nThe third element is the index of the the item in the Heap array.')
    print ('This allows us to locate its occurrence in the heap array in')
    print (' O(1) time, for efficient implementation of "reduceKey".')
    for i in range(5):
        print (Items[i])
    print ('----')
    print ('Initial sequence of elements in the heap array: ')
    print(P)

    # Reduce the key, shuffle the heap, and update the location variable in
    #  Items[3] to reflect its current position in the heap.
    P.reduceKey(Items[3], 3) 
    print ('---------')
    print ('State of the Items array after a reduceKey to key 3 on Items[3]\n')
    for i in range(5):
        print (Items[i])
    print ('----')
    print ('State of the heap array after this reduceKey operation:')
    print(P)
    print('---')
    print ('Changing the satellite information for Items[2] to be "purple"')
    Items[2]._value = 'purple'
    
    print ('----')
    print ('\nState of the Items array:\n')
    for i in range(5):
        print (Items[i])
    print ('----')
    print ('State of the heap array: ')
    print(P)
    print ('---')
    print ('extractMin on the heap returns', P.extractMin())
    print ('---')
    print ('State of heap after the extractMin: ')
    print(P)

