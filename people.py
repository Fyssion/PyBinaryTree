from tree import BinaryTree, Human
    


Clam = Human(5, "Clam", "clam")
Nator = Human(8, "Nator", "RoboNator")
Robot = Human(4, "Robot", "Robot Clam")
Nate = Human(6, "Nate", "Nathan")
Dave = Human(11, "Dave", "David")
Joe = Human(2, "Joe", "Joesef"")



people = BinaryTree()

people.insert(Clam)
people.insert(Nator)
people.insert(Robot)
people.insert(Nate)
people.insert(Dave)
people.insert(Joe)



print("----------\nBefore:")
people.print_tree()

Nator.nickname = "Robo.Nator" # Changing the name of Nator
people.replace(8, Nator)

print("----------\nAfter:")
people.print_tree()

print(f"---------\nLength: {people.length()}")



# result = people.find(int(input("ID to find: ")))
# if result is not None:
#     print(f"---ID: {result.id} | NAME: {result.name} | NICKNAME: {result.nickname}")
# else:
#     print("Not found.")
