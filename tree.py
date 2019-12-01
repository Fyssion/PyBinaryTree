class Human:
    """A human with attributes of id, name, and nickname."""
    def __init__(self, id, name, nickname):
        self.id = id
        self.name = name
        self.nickname = nickname

class CannotInsert(Exception):
    pass

# BinaryTree class 
class BinaryTree: 
   
    def __init__(self): 
        self.data = None 

        self.right = None
        self.left = None  


    def find(self, id):
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
        if isinstance(oldNode, Human):
            oldNode = oldNode.id
        


        

    def delete(self, node):
        if isinstance(node, Human):
            node = node.id

        if self.data.id > node:
            self.left = self.left.delete(node)
        elif self.data.id < node:
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
        if self.find(newData.id) is not None:
            # raise CannotInsert(f"Duplication Error: '{newData.id} - {newData.name}' could not be inserted. There is already a node with this ID!")
            return print(f"CannotInsert: There is already a node with an ID of {newData.id}")

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
    

    # Print the tree
    def PrintTree(self):
        if self.data is None:
            return print("Empty Tree")

        
        if self.left is not None:
            self.left.PrintTree()

        print(f"---\nID: {self.data.id}\nNAME: {self.data.name}\nNICKNAME: {self.data.nickname}")

        if self.right is not None:
            self.right.PrintTree()
   
    

Caleb = Human(5, "Caleb", "clam")
Grandpa = Human(8, "Grandpa", "bmw")
Yana = Human(4, "Yana", "yoyoyana")
Baba = Human(6, "Baba", "I can't think of a nickname for Baba")
Mom = Human(11, "Mom", "Ma")
Dad = Human(2, "Dad", "Da")



people = BinaryTree()

people.insert(Caleb)
people.insert(Grandpa)
people.insert(Yana)
people.insert(Baba)
people.insert(Mom)
people.insert(Dad)

print("Before:")
people.PrintTree()
people.delete(8)
print("After:")
people.PrintTree()

result = people.find(int(input("ID to find: ")))
if result is not None:
    print(f"---\nID: {result.id}\nNAME: {result.name}\nNICKNAME: {result.nickname}")
else:
    print("Not found.")
