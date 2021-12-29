##==============================================================
## Cuiyin Chen (20708813)
## CS 234 Spring 2019
## Assignment 04, Problem 2
##==============================================================

from math import floor

class Pair:
  
  def __init__(self, key, element):
    # Pair(key,element) returns a new key-element pair
    # __init__: Any Any -> Pair
    self._key = key
    self._element = element
  
  def get_key(self):
    # self.get_key() returns self's key
    # get_key: Pair -> Any
    return self._key
  
  def get_element(self):
    # self.get_element() returns self's element
    # get_element: Pair -> Any
    return self._element
  
  def __str__(self):
    # str(self) returns a string representation of self
    # __str__: Pair -> Str
    return "(" + str(self._key) + ", " + str(self._element) + ")"
  
def guess(low, high, search, length):
  # guess(low, high, search, length) produces a value from the formula
  # guess: Int Int Int Int -> Int
    return floor((search - low)/(high - low) * length)


class SortedArray:
    def __init__(self, capacity):
      # SortedArray(capacity) returns an empty sorted array that has space
      #   for capacity elements
      # __init__: Nat -> SortedArray
        self._items = [None] * capacity
        self._cap  = capacity
        self._size = 0
      
    def is_empty(self):
      # self.is_empty() produces True if self is empty; False otherwise
      # is_empty: SortedArray -> Bool
      return self._size == 0
    
    def __contains__(self,item):
      # item in self produces True if item is sorted in self; False otherwise
      # contains: SortedArray Any -> Bool
      return item in self._items
    
    def access(self,index):
      # self.access(index) returns the value stored at index
      # access: SortedArray Int -> Any
      return self._items[index]
    
    def add(self,item):
      # self.add(item) stores one instance of item in self
      # add: SortedArray Any -> None
      # Effect: item is stored in self
      self._items = self._items + [item]
      self._size += 1
    
    def delete(self,item):
      # self.delete(item) removes one instance of item in self
      # delete: SortedArray Any -> None
      # Effect: item is removed from self
      self._size -= 1
      self._items = self._items - [item]
    
    def linear_search(self,item):
      # self.linear_search(item) returns a pair. It keys is an index where
      #   item may be stored, and its element is the number of items 
      #   checked using a linear search
      # linear_search: SortedArray Any -> Pair
      pass
    
    def binary_search(self,item):
      # self.binary_search(item) returns a pair. It keys is an index where
      #   item may be stored, and its element is the number of items 
      #   checked using a binary search
      # binary_search: SortedArray Any -> Pair      
      pass
    
    def interpolation_search(self,item):
      # self.interpolation_search(item) returns a pair. It keys is an
      #   index where item may be stored, and its element is the number
      #   of items checked using a interpolation search
      # interpolation_search: SortedArray Any -> Pair      
      pass
        
