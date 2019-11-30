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


    def find(self, id):
        search = None
        if self.data.id == id:
            return self.data
        if self.left is not None:
            if self.left.data.id == id:
                return self.left.data
            search = self.left.find(id)
        if self.right is not None:
            if self.right.data.id == id:
                return self.right.data
            search = self.right.find(id)
        return search


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

result = people.find(int(input("ID to find: ")))
if result:
    print(f"---\nID: {result.id}\nNAME: {result.name}\nNICKNAME: {result.nickname}")
else:
    print("Not found.")
# people.PrintTree()