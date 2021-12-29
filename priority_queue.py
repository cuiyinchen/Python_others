##==============================================================
## Cuiyin Chen (20708813)
## CS 234 Spring 2019
## Assignment 04, Problem 1
##==============================================================
from binary_tree import *

class PriorityQueue:
  ''' Fields: _heap '''
  
  def __init__(self):
    # PriorityQueue() returns an empty PriorityQueue
    # __init__: Any -> PriorityQueue
    self._heap = BinaryTree()
  
  def is_empty(self):
    # self.is_empty() returns True if self is empty; False otherwise
    # is_empty: PriorityQueue -> Bool
    return self._heap == BinaryTree()
  
  def lookup_min(self):
    # self.lookup_min() returns the pair with minimun key in self
    # lookup_min: PriorityQueue -> Pair
    # Requires: key and elements can be of any type. keys are orderable though
    #   do not need to be distinct. And self is not empty.
    root = self._heap.get_root()
    min_key = self._heap.get_key(root)
    min_element = self._heap.get_element(root)
    return Pair(min_key, min_element)
  
  def add(self, key, element):
    # self.add(key, element) adds a pair (key,element) to self
    # add: PriorityQueue Any Any -> None
    # Effect: self is updated by adding a pair
    # Requires: key and elements can be of any type. keys are orderable though
    #   do not need to be distinct. 
    last = self._heap.next_leaf()
    self._heap.add_last(key,element)
    curr = last
    par = self._heap.get_parent(curr)
    while par != False and self._heap.get_key(curr) < self._heap.get_key(par):
      self._heap.swap_node_values(curr,par)
      curr = par
      par = self._heap.get_parent(curr)
    
    
  def delete_min(self):
    # self.delete_min() returns the pair with minimun key in self
    # delete_min: PriorityQueue -> Pair
    # Effect: removes the pair with minimun key in self
    # Requires: key and elements can be of any type. keys are orderable though
    #   do not need to be distinct. And self is not empty.
    root = self._heap.get_root()
    min_key = self._heap.get_key(root)
    min_element = self._heap.get_element(root)
    last = self._heap.get_last()
    self._heap.swap_node_values(last,root)
    self._heap.delete_last()
    last = self._heap.previous_leaf()
    curr = self._heap.get_root()
    left = self._heap.get_left(curr)
    right = self._heap.get_right(curr)
    key = self._heap.get_key(curr)
    stop = False
    while left != False and not stop:
      min_child = left
      if right != False and \
         self._heap.get_key(right) < self._heap.get_key(left):
        min_chiled = right
      if self._heap.get_key(min_child) < key:
        self._heap.swap_node_values(curr,min_child)
        curr = min_child
        left = self._heap.get_left(min_child)
        right = self._heap.get_right(min_child)
      else:
        stop = True
    return Pair(min_key,min_element)
