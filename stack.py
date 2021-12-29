

class Stack:
    def __init__(self):
        self._items = []
        self._size = 0
        
    def is_empty(self):
        return self._size == 0
    
    def push(self, data):
        self._items.append(data)
        self._size += 1
        
    def top(self):
        return self._items[self._size - 1]
    
    def pop(self):
        value = self.top()
        self._size -= 1
        self._items.pop(self._size)
        return value
#
