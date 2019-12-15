from tree import BinaryTree


# Creating a Human class to store data.
# Remember to include an ID variable when creating your own class.
class Human:
    """A human with attributes of id, name, and nickname."""
    def __init__(self, id, name, nickname):
        self.id = id
        self.name = name
        self.nickname = nickname


# Human(id, name, nickname)
# Creating example people to store
Clam = Human(5, "Clam", "clam")
Nator = Human(8, "Nator", "RoboNator")
Robot = Human(4, "Robot", "Robot Clam")
Nate = Human(6, "Nate", "Nathan")
Dave = Human(11, "Dave", "David")
Joe = Human(2, "Joe", "Joesef")
Jake = Human(7, "Jake", "Jaycoobee")


# Creating and initiating the BinaryTree
people = BinaryTree()

# Inserting people into the tree with insert()
people.insert(Clam)
people.insert(Nator)
people.insert(Robot)
people.insert(Nate)
people.insert(Dave)
people.insert(Joe)
people.insert(Jake)


# Printing the tree before and after replacing the data of a node
print("----------\nBefore:")
people.print_tree()

Nator.nickname = "Robo.Nator" # Changing the name of Nator
people.replace(8, Nator)

print("----------\nAfter:")
people.print_tree()

# Printing the length of a tree
print(f"---------\nLength: {people.length()}")

# Finding the distance to the farthest node
distance, data = people.dist_to_farthest()
print(f"Distance to farthest node: {distance} | Corresponding ID: {data.id}")


# Finding a node in the tree by ID
result = people.find(int(input("ID to find: ")))
if result is not None:
    print(f"---ID: {result.id} | NAME: {result.name} | NICKNAME: {result.nickname}")
else:
    print("Not found.")