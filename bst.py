##==============================================================
## Cuiyin Chen (20708813)
## CS 234 Spring 2019
## Assignment 03, Problem 1
##==============================================================


class Node:
    """
    Fields: _parent stores the parent node of self
            _left is the left child node of self
            _right is the right child node of self
            _key stores the key value of self
            _height is the height of the tree
    """
      
    def __init__(self, key, parent = None, left = None, right = None):
        # Node(key) produces a node set to None with the key 
        #   and empty parent without left and right child
        # Node: Any -> Node
        self._parent = parent
        self._left = left
        self._right = right
        self._key = key
        self._height = 0
            
    def get_key(self):
        # self.get_key() produces the key value of self
        # get_key: Node -> Any
        return self._key
    
    def get_parent(self):
        # self.get_parent() produces the parent node of self if any; 
        #   otherwise produces False
        # get_parent: Node -> (anyof Node Bool)
        if self._parent == None:
            return False
        return self._parent
    
    def get_right(self):
        # self.get_right() produces the right child node of self if any;
        #   else False
        # get_right: Node -> (anyof Node Bool)
        if self._right == None:
            return False
        return self._right
    
    def get_left(self):
        # self.get_left() produces the left child node of self if any;
        #   else False
        # get_left: Node -> (anyof Node Bool)
        if self._left == None:
            return False
        return self._left
    
    def get_height(self):
        # self.get_height() produces the height of self
        # get_height: Node -> Nat
        return self._height
    
    def set_key(self, key):
        # self.set_key(key) sets the key value of self to key
        # Effects: mutate self by setting the key value to a new key value
        # set_key: Node Any -> None
        return self._key
        
    def set_parent(self, parent):
        # self.set_parent(parent) sets the parent node of self to parent
        # Effects: mutate self by setting the parent node to new parent node
        # set_parent: Node Node -> None
        return self._parent
            
    def set_left(self, left):
        # self.set_left(left) sets the left node of self to left
        # Effects: mutate self by setting the left node to new left node
        # set_left: Node Node -> None
        self._left = left
        
    def set_right(self, right):
        # self.set_right(right) sets the right node of self to right
        # Effects: mutate self by setting the right node to new right node
        # set_right: Node Node -> None
        self._right = right
        
    def set_height(self, height):
        # self.set_height(height) sets the height value of self to height
        # Effects: mutate self by setting the height value to a new height value
        # set_height: Node Nat -> None
        self._height = height
    
    def __str__(self):
        # str(self) produces a string representation of a Node self
        # __str__: Node -> Str
        return str("(" + str(self._height) + ")" + " " + str(self._key))
    
    
class BST:
    """
    Fields: _root is the root of the BST
    """
        
    def __init__(self):
        # BST() produces an empty Binary Search Tree
        # BST: -> BST
        self._root = None
    
    def is_empty(self):
        # self.is_empty() produces True if self is empty; False otheriwse
        # is_empty: BST -> Bool
        if self._root == None:
            return True
        return False
    
    def get_root(self):
        # self.get_root() produces the root node of self
        # get_root: BST -> Node
        return self._root
    
    def get_height(self):
        # self.get_height() produces the height of self
        # get_height: BST -> Nat
        if self.is_empty():
            return -1
        return self._root.get_height()
    
    def get_key(self, node):
        # self.get_key(node) produces the key of node in self
        # get_key: BST Node -> Any
        return node.get_key()
    
    def search(self, key):
        # self.search(key) produces the node containing key. If no such 
        #   node, returns the potential parent node of key. If tree is
        #   empty, return None
        # search: BST Any -> (anyof Node None)
        if self.is_empty():
            return None
        curr = self._root
        prev = None
        while curr is not None:
            val = curr.get_key() # get key of current
            if val == key:
                return curr
            else:
                if key < val:
                    prev = curr
                    curr = curr.get_left()
                if key > val:
                    prev = curr
                    curr = curr.get_right()
        return prev
    
    def find_parent(self, key):
        # self.find_parent(key) produces the parent node of node
        #   containing key if parent exists; False otherwise. 
        #   If key is not in self, returns None
        # find_parent: BST Any -> (anyof Node Bool None)
        n = self.search(key)
        root = self._root
        if root == n:
            return False
        elif n.get_key() != key:
            return None
        else: # n.get_key() == key
            return n.get_parent()
        
    
    def find_left(self, key):
        # self.find_left(key) produces the left child of node containing key
        #   if the left child exists; False otherwise. If key not in self, 
        #   return False
        # find_left: BST Any -> (anyof Node Bool None)
        n = self.search(key)
        left = n.get_left() # either left child or False
        if n.get_key() == key:
            return left
        else: # n.get_key() != key => key is not in self
            return None
        
    
    def find_right(self, key):
        # self.find_right(key) produces the right child of node ontaining key 
        #   if its right child exists; False otherwise. 
        #   If key is not in self, return False
        # find_right: BST Any -> (anyof Node Bool None)
        n = self.search(key)
        right = n.get_right() # either right child or False
        if n.get_key() == key:
            return right
        else:  # n.get_key() != key => key is not in self
            return None
        
     
    def add_node(self, key):
        # self.add_node(key) inserts key in the correct place in self.
        #   And updates heights of affected nodes.
        # Effects: mutate self by inserting new key
        # add_node: BST Any -> None
        height = self.get_height()
        if self._root == None:    ## case then BST is empty
            self._root = Node(key)
            self._root.set_height(-1) 
        if self._root._key < key: ## should search on right side
            if self._root._right == None:
                self._root._right = Node(key)
                height += 1
                self._root.set_height(height)    
            else:
                pass
        else:                     ## key of root > key, should go to left side
            if self._root._left == None:                
                self._root._left = Node(key)
                print('left',self._root._left,Node(key))                
                height += 1
                self._root.set_height(height)                
            else:
                pass
                    
    def delete_node(self, key):
        # self.delete_node(key) deletes key from self and updates heights
        #   of affected nodes.
        # Effects: mutate self by deleting key from self
        # delete_node: BST Any -> None
        pass
    
    def traverse(self):
        # self.traverse() prints nodes in an in-order traversal.
        # Effects: prints the ndoes in self
        # traverse: BST -> None
        root = self._root
        if not self.is_empty():
            root._left.traverse()
            print(root._key)
            root._right.traverse()

