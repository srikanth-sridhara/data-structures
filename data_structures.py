import sys

class Node:
    """ This is a Node class that creates a linked list node """
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

    def getData(self):
        return self.data

    def setData(self, newdata):
        self.data = newdata

    def getNext(self):
        return self.next

    def setNext(self, newnext):
        self.next = newnext

class LinkedList:
    """ This is a Linked List class with all list methods implemented """
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def printLL(self):
        curr = self.head
        sys.stdout.write("-> ")
        while curr is not None:
            mystring = str(curr.getData()) + " --- "
            sys.stdout.write(mystring)
            sys.stdout.flush()
            curr = curr.getNext()
        print '|'

    def add(self, data):
        temp = Node(data)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.getNext()
        return count

    def search(self, data):
        temp = self.head
        while temp is not None:
            if temp.getData() == data:
                return True
            temp = temp.getNext()
        return False

    def remove(self, data_to_remove):
        prev = None
        curr = self.head
        while curr is not None:
            if curr.getData() == data_to_remove:
                if prev is None:
                    self.head = self.head.getNext()
                else:
                    prev.setNext(curr.getNext())
                return
            else:
                prev = curr
                curr = curr.getNext()

    def append(self, append_data):
        curr = self.head
        if curr is None:
            self.head = Node(append_data)
        else:
            while curr.getNext() is not None:
                curr = curr.getNext()
            curr.setNext(Node(append_data))

class Queue:
    """ This class creates a Queue and all its methods"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items is []

    def size(self):
        return len(self.items)

    def enqueue(self, data):
        self.items.insert(0, data)

    def dequeue(self):
        return self.items.pop()

    def printQueue(self):
        print "Rear->" + str(self.items) + "<-Front"

class Stack:
    """ This class creates a stack and all its methods"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items is []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def printStack(self):
        print str(self.items) + "<-Top of stack"

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self, key, size):
        return key%size

    def rehash(self, oldhash, size):
        return (oldhash+1)%size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))
        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] is key:
                self.data[hashvalue] = data
            else:
                newslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[newslot] is not None and self.slots[newslot] is not key:
                    newslot = self.rehash(newslot, len(self.slots))

                if self.slots[newslot] is None:
                    self.slots[newslot] = key
                    self.data[newslot] = data
                else:
                    self.data[newslot] = data

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))
        position = startslot
        while self.slots[position] is not None:
            if self.slots[position] is key:
                return self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position is startslot:
                    return None

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

class BinaryHeap:
    ''' creates a new, empty, binary heap. '''

    def __init__(self):
        ''' constructor '''
        self.heapList = []
        self.currentSize = 0

    def heapify(self, i):
        if i > self.currentSize:
            return
        leftChild = 2*i + 1
        rightChild = 2*i + 2

        smallest = i
        if leftChild < self.currentSize and \
            self.heapList[leftChild] < self.heapList[smallest]:
            smallest = leftChild
        if rightChild < self.currentSize and \
            self.heapList[rightChild] < self.heapList[smallest]:
            smallest = rightChild
        if i is not smallest:
            self.heapList[i], self.heapList[smallest] = self.heapList[smallest], self.heapList[i]
            self.heapify(smallest)

    def percolateUp(self, i):
        myindex = i
        paindex = (myindex-1)//2
        while paindex >= 0:
            if self.heapList[myindex] < self.heapList[paindex]:
                self.heapList[myindex], self.heapList[paindex] = self.heapList[paindex], self.heapList[myindex]
            myindex = paindex
            paindex = (paindex -1)//2

    def insert(self, k):
        ''' adds a new item to the heap. '''
        self.heapList.append(k)
        self.currentSize += 1
        self.percolateUp(self.currentSize-1)
        print self.heapList

    def findMin(self):
        ''' returns the item with the minimum key value, leaving item in the heap. '''
        return self.heapList[0]

    def delMin(self):
        ''' returns the item with the minimum key value, removing the item from the heap. '''
        mindata = self.findMin()
        self.currentSize -= 1
        self.heapList[0] = self.heapList[self.currentSize]
        self.heapList.pop()
        self.heapify(0)
        return mindata

    def isEmpty(self):
        ''' returns true if the heap is empty, false otherwise. '''
        return self.currentSize is 0

    def size(self):
        ''' returns the number of items in the heap. '''
        return self.currentSize

    def buildHeap(self, inputlist):
        ''' builds a new heap from a list of keys. '''
        for el in inputlist:
            self.insert(el)

class BinarySearchTree:
    '''docstring for BinarySearchTree'''
    def __init__(self):
        ''' Init function '''

    def Map(self):
        ''' Create a new, empty map. '''

    def put(self, key, val):
        ''' Add a new key-value pair to the map. If the key is already '''
        ''' in the map then replace the old value with the new value.  '''

    def get(self, key):
        ''' Given a key, return the value stored in the map or None otherwise. '''

    def delete(self):
        ''' Delete the key-value pair from the map using a statement of the form del map[key]. '''

    def len(self):
        ''' Return the number of key-value pairs stored in the map. '''

    def exists(self, key):
        ''' Return True for a statement of the form key in map, if the given key is in the map.'''

# **************************************************************** #

def test_linked_list():
    mylist = LinkedList()
    print "Adding a few elements to Linked list: 31,77,17,93,26,54"
    mylist.printLL()
    mylist.add(31)
    mylist.printLL()
    mylist.add(77)
    mylist.printLL()
    mylist.add(17)
    mylist.printLL()
    mylist.add(93)
    mylist.printLL()
    mylist.add(26)
    mylist.printLL()
    mylist.add(54)
    mylist.printLL()

    print("Size of linked list is: " + str(mylist.size()))
    print("Searching for element 93: " + str(mylist.search(93)))
    print("Searching for element 100: " + str(mylist.search(100)))
    print "removing elements 54, then 93 and then 31"
    mylist.remove(54)
    mylist.remove(93)
    mylist.remove(31)
    print("New Size: " + str(mylist.size()))
    mylist.printLL()
    print "Appending 35, 36, 37 and 38 to the linked list"
    mylist.append(35)
    mylist.append(36)
    mylist.append(37)
    mylist.append(38)
    mylist.printLL()

def test_binary_search_tree():
    # myBst = BinarySearchTree()
    print "This is still TODO"

def test_queue():
    myQueue = Queue()
    print "Adding elements 10,20,30,40,50 to queue (enqueue)"
    myQueue.enqueue(10)
    myQueue.printQueue()
    myQueue.enqueue(20)
    myQueue.printQueue()
    myQueue.enqueue(30)
    myQueue.printQueue()
    myQueue.enqueue(40)
    myQueue.printQueue()
    myQueue.enqueue(50)
    myQueue.printQueue()
    print "Removing elements one by one from the queue (dequeue)"
    myQueue.dequeue()
    myQueue.printQueue()
    myQueue.dequeue()
    myQueue.printQueue()
    myQueue.dequeue()
    myQueue.printQueue()
    myQueue.dequeue()
    myQueue.printQueue()
    myQueue.dequeue()
    myQueue.printQueue()

def test_stack():
    mystack = Stack()
    print "Adding elements 10,20,30,40,50 to stack (push)"
    mystack.push(10)
    mystack.printStack()
    mystack.push(20)
    mystack.printStack()
    mystack.push(30)
    mystack.printStack()
    mystack.push(40)
    mystack.printStack()
    mystack.push(50)
    mystack.printStack()
    print "Removing elements one by one from the stack (pop)"
    mystack.pop()
    mystack.printStack()
    mystack.pop()
    mystack.printStack()
    mystack.pop()
    mystack.printStack()
    mystack.pop()
    mystack.printStack()
    mystack.pop()
    mystack.printStack()

def test_hash_table():
    H=HashTable()
    print"Created an empty hash table:"
    print "Slots: {}".format(H.slots)
    print "Data : {}".format(H.data)
    H[54]="cat"
    H[26]="dog"
    H[93]="lion"
    H[17]="tiger"
    H[77]="bird"
    H[31]="cow"
    H[44]="goat"
    H[55]="pig"
    H[20]="chicken"
    print "After adding a bunch of key value pairs:"
    print "Slots: {}".format(H.slots)
    print "Data : {}".format(H.data)

def test_binary_heap():
    bh = BinaryHeap()
    print "Creating a binary heap with the values: 5,7,3,11 in that order"
    bh.insert(5)
    bh.insert(7)
    bh.insert(3)
    bh.insert(11)

    print "Deleting the minimum element in the heap one by one"
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())

def parse_main():
    print "Welcome to Python Data Structures."
    print "Here are your options:"
    print "1) Linked List"
    print "2) Binary Search Tree"
    print "3) Queue"
    print "4) Stack"
    print "5) Hash Table"
    print "6) Binary Heap"

    choice = int(raw_input())
    if choice is 1:
        test_linked_list()
    elif  choice is 2:
        test_binary_search_tree()
    elif  choice is 3:
        test_queue()
    elif  choice is 4:
        test_stack()
    elif  choice is 5:
        test_hash_table()
    elif  choice is 6:
        test_binary_heap()
    else:
        print "Please choose a number between 1 and 6"

if __name__ == "__main__":
    parse_main()
