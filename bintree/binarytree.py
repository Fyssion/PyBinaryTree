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

class EmptyTreeError(Exception):
    """Raised when the Tree is Empty"""


class Node:
    """
    A node in a Binary Tree.

    Once initiated, the node remains empty until a node is inserted.
    A node is inserted/sorted with its ID.

    You can insert, delete, replace, or find a node in the binary tree.
    You can print the entire binary tree from left to right with print_tree().
    """

    def __init__(self):
        """Initiate the tree. Tree is empty until a node is inserted."""

        self.data = None

        self.right = None
        self.left = None
        self.parent = None

        self._add_aliases()

    def _add_aliases(self):
        """
        NOT TO BE USED (other than in the __init__ function)!
        Seperate function that adds aliases to functions.
        """
        self.dist_to_farthest = self.depth
        self.delete = self.remove
        self.search = self.find

    def find_node(self, id):
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
            search = self

        return search

    def find(self, id):
        """Same as find_node() but returns data instead of node itself."""
        return self.find_node(id).data

    def replace(self, oldNode, newNode):
        """
        Replace a node in the tree.

        Parameters:
        -oldNode: The id (or node object) of the node you want to replace.
        -newNode: The new node (data object) you want to replace the old node with.

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

    def remove(self, node):
        """
        Remove a node from the tree.

        Parameters:
        -node: The node you want to remove (id or data object)
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

                    self.left = Node()
                    self.left.insert(newData)
                    self.left.parent = self

                else:
                    self.left.insert(newData)

            elif newData.id > self.data.id:
                if self.right is None:

                    self.right = Node()
                    self.right.insert(newData)
                    self.right.parent = self

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

    def depth(self):
        """
        Calculates the distance to the farthest node and returns it's data.

        Returns the distance and the farthest node's data.
        """

        distance = 1

        if self.right is not None:
            rightDist, rightData = self.right.dist_to_farthest()
        else:
            rightDist = None

        if self.left is not None:
            leftDist, leftData = self.left.dist_to_farthest()
        else:
            leftDist = None

        if rightDist is None or leftDist is None:

            if rightDist is None and leftDist is None:
                return 0, self.data # Returning 0 so the distance counts up from 0

            if rightDist is None:
                distance += leftDist
                return distance, leftData

            elif leftDist is None:
                distance += rightDist
                return distance, rightData

        if rightDist > leftDist:
            distance += rightDist
            return distance, rightData

        else:
            distance += leftDist
            return distance, leftData

    # def  queue_tree(self):
    #     queue = []

    #     queue.append(self.data)
    #     if self.left:
    #         queue.append(self.left.queue_tree())
    #     else:
    #         queue.append(None)
    #     if self.right:
    #         queue.append(self.right.queue_tree())
    #     else:
    #         queue.append(None)

    #     return queue

    def display(self):
        if self.data is None:
            print("Empty Tree")
            return
        queue = []
        tree = {}
        level = 0
        queue.append(self)

        allNotNone = True
        while allNotNone and level  < 6:
            tree[level] = []
            for i in range(2**level):
                parentNode = queue.pop(0)

                if parentNode is None:
                    tree[level].append(" ")
                    queue.append(None)
                    queue.append(None)
                    # print(f"PNode: None | Queue: {queue} | Level: {level}")
                else:
                    tree[level].append(f"{parentNode.data.id}")
                    queue.append(parentNode.left)
                    queue.append(parentNode.right)
                    # print(f"PNode: {parentNode.data.id} | Queue: {queue} | Level: {level}")


            if all(item is None for item in queue):
                allNotNone = False
                # break
            level += 1

        # n = len(tree)
        # for i in range(len(tree)):

        #     n -= 1
        #     for z in range((2**n)):
        #         tree[i] = " " + tree[i]

            # for n in range(len(tree)):
            #     for z in range((2**i) // 2):
            #         tree[i] = " " + tree[i]

        largestNumLength = 0
        for i in range(len(tree)):
            for x in range(len(tree[i])):
                tempLength = len(tree[i][x])
                if tempLength > largestNumLength:
                    largestNumLength = tempLength

        def pad(string: str, padding: int):
            if len(string) < padding:
                for i in range(padding - len(string)):
                    string += " "
            return string

        spacing = [1, 3, 7, 15, 31, 63, 124, 255, 511, 1023]

        # Formula that calculates the spacing list above
        # num = 1
        # spacing = [1]
        # for i in range(9):
        #     ans = num+num+1
        #     num = ans
        #     spacing.append(ans)

        if largestNumLength == 1:
            space = " "
            spacingMulti = 2
        elif largestNumLength == 2:
            spacingMulti = 1
            space = "  "
        else:
            print("Cannot print tree. IDs are more than two characters wide.")
            return

        n = len(tree) - 1
        for i in range(len(tree)):
            for v in range(len(tree[i])):
                tree[i][v] = tree[i][v].rjust(largestNumLength)
                for z in range(spacing[n]):
                    tree[i][v] += space
            n -= 1
        output = ""
        n = len(tree)
        for i in range(len(tree)):
            levelOut = "".join(tree[i])
            for z in range(n - 1):
                levelOut += "\n"
            for z in range((2**n) // spacingMulti):
                levelOut = " " + levelOut
            output += levelOut
            n -= 1

        print(output)
        dist, node = self.dist_to_farthest()
        if dist > 5:
            print("WARNING: ONLY PRINTED LEVELS 0-5")        # print("\n".join(tree))

            # queue.append(parentNode)
            # if parentNode.left is None and parentNode.right is None:
            #     allNotNone = False
            #     break
            # if parentNode.left is not None:
            #     queue.append(parentNode.left)
            # if parentNode.right is not None:
            #     queue.append(parentNode.right)

    def print_tree(self):
        """Prints out the tree from left to right."""

        if self.data is None:
            return print("Empty Tree")

        if self.left is not None:
            self.left.print_tree()

        print(f"---ID: {self.data.id} | NAME: {self.data.name} | NICKNAME: {self.data.nickname}")

        if self.right is not None:
            self.right.print_tree()


class BinaryTree(Node):
    """
    This absolute piece of trash is my lazy approach to making a better tree.

    I'll rewrie it soon. I hope.
    """
    def __init__(self):
        self.root = None

        self._add_aliases()

    def find_node(self, id):
        if self.root is not None:
            return self.root.find_node(id)

    def find(self, id):
        """Same as find_node() but returns data instead of node itself."""
        return self.find_node(id)

    def insert(self, newData):
        if self.root is not None:
            self.root.insert(newData)
        else:
            self.root = Node()
            self.root.insert(newData)

    def remove(self, node):
        if self.root is not None:
            self.root.remove(node)
        else:
            raise EmptyTreeError("Tree is empty. There is nothing to remove.")

    def replace(self, oldData, newData):
        if self.root is not None:
            self.root.replace(oldData, newData)
        else:
            raise EmptyTreeError("Tree is empty. There is nothing to replace.")

    def length(self):
        if self.root is not None:
            return self.root.length()

    def depth(self):
        if self.root is not None:
            return self.root.depth()

    def display(self):
        if self.root is not None:
            self.root.display()

    def print_tree(self):
        if self.root is not None:
            self.root.print_tree()
