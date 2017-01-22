class Node(object):

    def __init__(self, value, parent=None, left=None, right=None):

        self.value = value
        self.left, self.right = left, right
        self.parent = parent

    def contains(self, value):

        if value == self.value:
            return True

        if value > self.value:
            return False if self.right is None else self.right.contains(value)

        if value < self.value:
            return False if self.left is None else self.left.contains(value)

    def add_child(self, value):

        if value == self.value:
           return 

        if value > self.value:

            if self.right is None:
                self.right = Node(value, parent=self)
            else:
                self.right.add_child(value)

        else:

            if self.left is None:
                self.left = Node(value, parent=self)
            else:
                self.left.add_child(value)

    def _find_maximum_subtree_child_value(self):

        current_node = self

        while current_node.right is not None:
            current_node = current_node.right

        return current_node.value

    def _find_minimum_subtree_child_value(self):

        current_node = self

        while current_node.left is not None:
            current_node = current_node.left

        return current_node.value

    def _find_in_order_successor(self):

        if self.right is None:
            # TO-DO: Handle case where parent is actually in-order
            # successor.
            return None

        return self.right._find_minimum_subtree_child_value()

    def _find_in_order_predecessor(self):

        if self.left is None:
            
            return None 

        return self.left._find_maximum_subtree_child_value()

    def remove_value(self, value):

        if value == self.value:

            if self.left is None and self.right is None:
                return None

            if self.left is None and self.right is not None:
                self.right.parent = self.parent
                return self.right

            if self.right is None and self.left is not None:
                self.left.parent = self.parent
                return self.left
            
            if self.right is not None and self.left is not None:
                self.value = self._find_in_order_successor()
                self.right = self.right.remove_value(child)
                return self

        else:

            self.left = self.left.remove_value(value) if self.left is not None else self.left
            self.right = self.right.remove_value(value) if self.right is not None else self.right
            return self

    def __repr__(self):
        return "Node(value={0}, right={1}, left={2})".format(self.value, self.right, self.left)

    def __str__(self):
        return self.__repr__()

class BinarySearchTree(object):

    def __init__(self, value=None):
        self.head = None if value is None else Node(value)

    def add_value(self, value):

        if self.head is None:
           self.head = Node(value)
        else:
           self.head.add_child(value)

    def contains(self, value):
        return self.head.contains(value)

    def remove_value(self, value):
        self.head = self.head.remove_value(value)
    
    def __repr__(self):
        return repr(self.head)

def ConsistentHashRingBST(object):

   def find_nearest_neighbour(self, value): 

       minimum_value = self.head._find_minimum_subtree_child_value()
       
       # state may be one of ('<', '>')

       state = '>'
       current_node = self.head

       while True:
       
           if state == '>':

               if current_node.value < value:

                   if not current_node.right:
                       current_node = minimum_value
                       break

                   else:
                       current_node = current_node.right
               
               
