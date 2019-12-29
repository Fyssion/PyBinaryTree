# PyBinaryTree

Personal project to learn how binary trees work.

## Documentation (OUTDATED)

^^ Working on making self-updating documentation or whatever. Make the computer do it for me.

This is less of an actual documentation and more of a way for me to learn how to write good documentation.

**Note: You can store any object in the binary tree as long as the object contains an `ID` variable.**

### `class tree.BinaryTree()`

### Variables

`data` - The object that is storing data. **Object must have an `ID` variable**

`right` - The node to the right of the current node

`left` - The node to the left of the current node.

**Right and left should not be set manually. Instead, see [insert()](#insertnewdata).**

### Functions

#### `find(id)`

    Find a node in the tree. Returns node or None if not found.
        
    Parameters:
    -ID: The ID of the node you want to find

#### `replace(oldNode, newNode)`

    Replace a node in the tree.
    Parameters:
    -oldNode: The id (or node object) of the node you want to replace.
    -newNode: The new node (node object) you want to replace the old node with.
    oldNode and newNode MUST have the same id!

#### `delete(node)`

    Delete a node from the tree.
    Parameters:
    -node: The node you want to delete (id or node object)

#### `insert(newData)`

    Insert a node into the tree.
    Parameters:
    -newData: The new node (node object) to insert.
    The ID of newData CANNOT already be in the tree. 

#### `length()`

    Returns length of tree (int).

#### `dist_to_farthest()`

    Calculates the distance to the farthest node and returns it's data.
        
    Returns the distance and the farthest node's data.

#### `print_tree()`

    Prints out the tree from left to right.
