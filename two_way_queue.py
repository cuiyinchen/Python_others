##==============================================================
## Cuiyin Chen (20708813)
## CS 234 Spring 2019
## Assignment 02, Problem 3
##==============================================================

# Question 3
# Queue ADT using double linked list with running time theta(1)
# TwoWayQueue: allows elements to be added and removed from both 
#    ends of the Queue
class Node:
    """
    Fields: _value stores any value
            _next points to the next node in the list
            _prev points to the previous node in the list
    """

    ## Node(value) produces a newly constructed doubly-linked node
    ##     storing value.
    ## __init__: Any -> Node
    def __init__(self, value, next = None, prev = None):
        self._value = value
        self._next = next
        self._prev = prev

    ## repr(self) produces a string with the information in self.
    ## __repr__: Node -> Str
    def __repr__(self):
        if self._value == None:
            return "Empty node"
        else:
            return str("Node containing " + self._value)

    ## self.access() produces the value stored in self.
    ## access: Node -> Any
    def access(self):
        return self._value

    ## self.next() produces the node to which self is linked
    ##    using next or None if none exists.
    ## next: Node -> (anyof Node None)
    def next(self):
        return self._next

    ## self.prev() produces the node to which self is linked
    ##    using prev or None if none exists.
    ## next: Node -> (anyof Node None)
    def prev(self):
        return self._prev

    ## self.store(value) stores value in self.
    ## Effects: Mutates self by storing value in self.
    ## store: Node, Any -> None
    def store(self, value):
        self._value = value

    ## self.link_next(node) links node using the next pointer.
    ## Effects: Mutates self by linking node using the next pointer.    
    ## link: Node (anyof Node None) -> none
    def link_next(self, node):
        self._next = node

    ## self.link_prev(node) links node using the prev pointer.
    ## Effects: Mutates self by linking node using the prev pointer.
    ## link: Node (anyof Node None) -> none
    def link_prev(self, node):
        self._prev = node

########################    

class TwoWayQueue:
    """    
    Fields: _head points to the first node of the TwoWayQueue
            _tail points to last node of the TwoWayQueue
            _size is the number of nodes in the TwoWayQueue

    """    
    
    # TwoWayQueue() produces an empty TwoWayQueue
    # __init__: -> TwoWayQueue    
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
    # self.is_empty() produces True if self is empty; otherwise False
    # is_empty: TwoWayQueue -> Bool
    def is_empty(self):
      #  print(self._size)
        return self._size <= 0 or (self._head == None and self._tail == None)
    
    # self.first() returns the first element in self
    # first: TwoWayQueue -> Any
    # Require: self is not empty
    def first(self):
        if self._size == 0:
            return
        return self._head._value
    
    # self.last() returns the last element in self
    # last: TwoWayQueue -> Any
    # Require: self is not empty
    def last(self):
        if self._size <= 0:
            return
        return self._tail._value
    
    # self.enqueue_first(data) modifies self and add data as first element in 
    #    self; returns none
    # Effects: modifies self
    # enqueue_first: TwoWayQueue Any -> None
    def enqueue_first(self, data):
        new_node = Node(data)

        if self._size <= 0:
            self._tail = new_node
            self._head = new_node
            
        self._size += 1
        
        self._head._prev = new_node
        new_node._next = self._head
        self._head = new_node            
                      
    
    # self.dequeue_first() returns the first element in self; and modifies
    #    to remove the first element from self
    # Effects: modifies self
    # dequeue_first: TwoWayQueue -> Any
    # Require: self is not empty
    def dequeue_first(self):
        if self._head == None:
            return
        first_element = self._head._value
        self._head = self._head._next
        self._size -= 1
        
        return first_element
    
    # self.enqueue_last(data) modifies self and add data as last element;
    #    returns none
    # Effects: modify self
    # enqueue_last: TwoWayQueue Any -> None    
    def enqueue_last(self, data):
        new_node = Node(data)
        
        if self._size == 0:
            self._tail = new_node
            self._head = new_node
        
        self._size += 1
    
        self._tail._next = new_node
        new_node._prev = self._tail
        self._tail = new_node            
        
              
    # self.dequeue_last() returns the last element in self; and modifies
    #    to remove the last element from self
    # dequeue_last: TwoWayQueue -> Any
    # Require: self is not empty
    def dequeue_last(self):
        if self._tail == None:
            return
        last_element = self._tail._value
        self._tail = self._tail._prev
        self._size -= 1
        return last_element
    
    # self.shift_first() modifies to move the first element in self to the 
    #    end of self
    # Effects: modifies self
    # shift_first: TwoWayQueue -> None
    # Require: self is not empty
    def shift_first(self):
        first_element = self._head._value
        self.dequeue_first()
        self.enqueue_last(first_element)
    
    # self.shift_last() modifies to move the last element in self to the 
    #    front of self
    # Effects: modifies self    
    # shift_last: TwoWayQueue -> None
    # Require: self is not empty
    def shift_last(self):
        last_element = self._tail._value
        self.dequeue_last()
        self.enqueue_first(last_element)
               
    
    # self.dequeue_all() removes all elements from self
    # Effects: modifies self by removing all elements from self    
    # dequeue_all: TwoWayQueue -> None
    def dequeue_all(self):
        if self._size == 0:
            return
        else:
            self.dequeue_first()
            self.dequeue_all()


## Testing. this is not part of the solutions
#n = Node(1)
#n.store('a')
            
#n2 = Node('2')
#n3 = Node(3)    
    
#t = TwoWayQueue()
#t.is_empty()
#t.enqueue_first('5')
#t.enqueue_first('4')
#t.enqueue_first('3')
#t.enqueue_first('1')
#t.enqueue_last(n2)
# so it is 1, 3, 4, 5, Node containing 2

#a = TwoWayQueue()
#a.is_empty()
#a.enqueue_first('d')
#a.last() #=> 'd'
#a.first() #=> 'd'
#a.dequeue_first() #=> 'd'
#a.first() #=> error
#a.last() #=> 'd'
