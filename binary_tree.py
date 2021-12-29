##==============================================================
## Cuiyin Chen (20708813)
## CS 234 Spring 2019
## Assignment 04, Problem 1
##==============================================================

class Pair:
  """ fields: _key and _element """
  
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
  
  
INFINITY = 100

class BinaryTree:
  def __init__(self):
    # BinaryTree() returns an empty Binary Tree
    # __init__: -> BinaryTree
    self._A = [None] * INFINITY
    self._Last = -1
    
  def get_root(self):
    # self.get_root() produces the root node of self
    # get_root: BinaryTree -> Pair
    return self._A[0]
  
  def is_empty(self):
    # self.is_empty() produces True if self is empty; False otherwise
    # is_empty: BinaryTree -> Bool    
    return self._Last == -1
  
  def get_key(self, node):
    # self.get_key(node) produces the key of node in self
    # get_key: BinaryTree Node -> Any
    return self._A[node].get_key()
  
  def get_element(self, node):
    # self.get_element(node) produces the element of node in self
    # get_element: BinaryTree -> Any
    return self._A[node].get_element()
  
  def get_parent(self, node):
    # self.get_parent(node) produces the parent node of node if it exists;
    #   False otherwise
    # get_parent: BinaryTree Node -> Anyof(Pair Bool)
    ##???
    if self.get_left(self.get_root()) == False and \
       self.get_right(self.get_root()) == False:
      return False
    return int(0.5*(node-1))
  
  def get_left(self, node):
    # self.get_left(node) produces the left child node of node if it exists;
    #   False otherwise
    # get_left: BinaryTree Node -> Anyof(Pair Bool)
    if (1+2*node) > self.get_last():
      return False
    return (1+2*node)
  
  def get_right(self, node):
    # self.get_right(node) produces the right child node of node if it exists;
    #   False otherwise
    # get_right: BinaryTree Node -> Anyof(Pair Bool)    
    if (2+2*node) > self.get_last():
      return False
    return (2+2*node)
  
  def get_last(self):
    # self.get_last() produces the location of the last leaf in self
    # get_last: BinaryTree -> Int
    return self._Last
  
  def next_leaf(self):
    # self.next_leaf() produces the location of the last leaf in self if 
    #   a new leaf was added
    ## if new leaf added???
    # next_leaf: BinaryTree -> Int
    return 1+self._Last
  
  def previous_leaf(self):
    # self.previous_leaf() returns the location of what would be the last leaf
    #   in self if the last leaf was removed
    # previous_leaf: BinaryTree -> Int
    return self._Last - 1
  
  def swap_node_values(self, node1, node2):
    # self.swap_node_values(node1,node2) swaps the key-element pairs stored in
    #   node1 and node2 in self
    # swap_node_values: BinaryTree Node Node -> None
    # Effects: key-element pairs are swapped in node1 and node2
    newnode1 = Pair(self.get_key(node1),self.get_element(node1))
    newnode2 = Pair(self.get_key(node2),self.get_element(node2))
    self._A[node1] = newnode1
    self._A[node2] = newnode2
    
    
  def add_last(self, key, element):
    # self.add_last(key,element) adds a key-element pair in self at the next 
    #   leaf position
    # add_last: BinaryTree Any Any -> None
    # Effects: new pair added to self
    p = Pair(key,element)
    self._Last += 1
    self._A[self.next_leaf()] = p
    
  def delete_last(self):
    # self.delete_last() deletes the last leaf in self
    # delete_last: BinaryTree -> None
    # Effects: last leaf is deleted in self
    self._Last -= 1
    self._A[self.get_last()] = None
  
  def level_order(self,node):
    # self.level_order(node) prints out the nodes of the subtree of self 
    #   rooted at node
    # lever_order: BinaryTree Node -> None
    # Effects: each node's information (key,element) in self is printed out
    #   on a separate line using lever-order traversal
    if node != None:
      print(self._A[node])
      self.level_order(self.get_left(node))
      self.lever_order(self.get_right(node))
    
  def traverse(self):
    # self.traverse() prints out the nodes in a level-order traversal
    # traverse: BinaryTree -> None
    # Effects: each node's information (key,element) in the subtree is
    #   printed out on a separate line using lever-order traversal
    self.level_order(self.get_root())
