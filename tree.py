class Human:
    def __init__(self, id, name, nickname):
        self.id = id
        self.name = name
        self.nickname = nickname

# BinaryTree class 
class BinaryTree: 
   
    def __init__(self, data): 
        self.data = data 

        self.right = None
        self.left = None  
                

    def insert(self, newData):
        if self.data:
            if newData.id < self.data.id:
                if self.left is None:
                    self.left = BinaryTree(newData)
                else:
                    self.left.insert(newData)
            elif newData.id > self.data.id:
                if self.right is None:
                    self.right = BinaryTree(newData)
                else:
                    self.right.insert(newData)
        else:
            self.data = data
    

    # Print the tree
    def PrintTree(self):
        if self.left is not None:
            self.left.PrintTree()
        print(f"---\nID: {self.data.id}\nNAME: {self.data.name}\nNICKNAME: {self.data.nickname}")
        if self.right is not None:
            self.right.PrintTree()
   
    

Caleb = Human(5, "Caleb", "clam")
Grandpa = Human(8, "Grandpa", "bmw")
Yana = Human(4, "Yana", "yoyoyana")
Baba = Human(11, "Baba", "I can't think of a nickname for Baba")


people = BinaryTree(Caleb)

people.insert(Grandpa)
people.insert(Yana)
people.insert(Baba)

people.PrintTree()