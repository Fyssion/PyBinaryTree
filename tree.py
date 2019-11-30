class Human:
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
Baba = Human(11, "Baba", "I can't think of a nickname for Baba")
Mom = Human(4, "Mom", "Ma")



people = BinaryTree()

people.insert(Caleb)
people.insert(Grandpa)
people.insert(Yana)
people.insert(Baba)
people.insert(Mom)

people.PrintTree()

result = people.find(int(input("ID to find: ")))
if result:
    print(f"---\nID: {result.id}\nNAME: {result.name}\nNICKNAME: {result.nickname}")
else:
    print("Not found.")