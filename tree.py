# Create Error Types
class DuplicateError(Exception):
    """Raised when there is a duplicate of a node."""
    pass
class NodeDoesNotExist(Exception):
    """Raised when a node does not exist."""
    pass
class IDsDoNotMatch(Exception):
    """Raised when two IDs do not match."""
    pass

# BinaryTree class 
class BinaryTree: 
    """
    Binary Tree that contains nodes.

    Once initiated, the binary tree remains empty until a node is inserted.
    A node is inserted/sorted with its ID.

    You can insert, delete, replace, or find a node in the binary tree.
    You can print the entire binary tree from left to right with print_tree().
    """
   
    def __init__(self):
        """Initiate the tree. Tree is empty until a node is inserted."""

        self.data = None 

        self.right = None
        self.left = None  


    def find(self, id):
        """
        Find a node in the tree. Returns node or None if not found.
        
        Parameters:
        -ID: The ID of the node you want to find.
        """

        if self.data is None:
            return None

        search = None

        if id > self.data.id:
            if self.right is not None:
                search = self.right.find(id)
            else:
                return None
        elif id < self.data.id:
            if self.left is not None:
                search = self.left.find(id)
            else:
                return None
        if id == self.data.id:
            search = self.data

        return search
        

    def replace(self, oldNode, newNode):
        """
        Replace a node in the tree.

        Parameters:
        -oldNode: The id (or node object) of the node you want to replace.
        -newNode: The new node (node object) you want to replace the old node with.

        oldNode and newNode MUST have the same id!
        """

        if type(oldNode) != int:
            try:
                oldNode = oldNode.id
            except AttributeError:
                raise TypeError("Old node must be an int or an object with an 'id' variable.")

        if oldNode != newNode.id:
            raise IDsDoNotMatch(f"Cannot replace node. Old node and replacement must have the same ID. Use delete() and insert() to add/delete IDs.")
            return print("Old node and replacement must have the same ID! Use delete and insert to add/delete IDs.")

        if self.find(oldNode) is None:
            raise NodeDoesNotExist(f"Cannot replace node. Node {oldNode} does not exist. Use insert() to add new nodes")
            return print("Cannot replace node. Node does not exist. Use insert to add nodes.")

        if oldNode < self.data.id:
            self.left.replace(oldNode, newNode)
        elif oldNode > self.data.id:
            self.right.replace(oldNode, newNode)
        else:
            self.data = newNode

        

    def delete(self, node):
        """
        Delete a node from the tree.

        Parameters:
        -node: The node you want to delete (id or node object)
        """

        if type(node) != int:
            try:
                node = node.id
            except AttributeError:
                raise TypeError("Node must be an int or an object with an 'id' variable.")

        if self.find(node) is None:
            raise NodeDoesNotExist(f"Cannot delete node. Node {node} does not exist. Use insert() to add new nodes")
            return print("Cannot delete node. Node does not exist. Use insert to add nodes.")

        if node < self.data.id:
            self.left = self.left.delete(node)
        elif node > self.data.id:
            self.right = self.right.delete(node)
        else:
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            
            temp_node = self.right
            minimum_data = temp_node.data

            while temp_node.left is not None:
                temp_node = temp_node.left
                minimum_data = temp_node.data
            
            self.data = minimum_data

            self.right = self.right.delete(self.data)

            return self



    def insert(self, newData):
        """
        Insert a node into the tree.

        Parameters:
        -newData: The new node (node object) to insert.

        The ID of newData CANNOT already be in the tree. 
        """

        if self.find(newData.id) is not None:
            # Raise a duplicate error
            raise DuplicateError(f"There is already a node with the ID of {newData.id}")
            return print(f"DuplicateError: There is already a node with the ID of {newData.id}")

        if self.data:

            if newData.id < self.data.id:
                if self.left is None:

                    self.left = BinaryTree()
                    self.left.insert(newData)

                else:
                    self.left.insert(newData)
            
            elif newData.id > self.data.id:
                if self.right is None:

                    self.right = BinaryTree()
                    self.right.insert(newData)

                else:
                    self.right.insert(newData)

        else:
            self.data = newData

    
    def length(self):
        """Returns length of tree (int)."""

        if self.data is None:
            return 0

        if self.left is not None:
            leftCounter = self.left.length()
        else:
            leftCounter = 0
        
        if self.right is not None:
            rightCounter = self.right.length()
        else:
            rightCounter = 0

        counter = leftCounter + 1 + rightCounter

        return counter
    

    # Print the tree
    def print_tree(self):
        """Prints out the tree from left to right."""

        if self.data is None:
            return print("Empty Tree")

        
        if self.left is not None:
            self.left.print_tree()

        print(f"---ID: {self.data.id} | NAME: {self.data.name} | NICKNAME: {self.data.nickname}")

        if self.right is not None:
            self.right.print_tree()