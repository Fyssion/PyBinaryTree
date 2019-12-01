from tree import BinaryTree, Human
import tree
    


Caleb = Human(5, "Caleb", "clam")
Grandpa = Human(8, "Grandpa", "bmw")
Yana = Human(4, "Yana", "yoyoyana")
Baba = Human(6, "Baba", "I can't think of a nickname for Baba")
Mom = Human(11, "Mom", "Ma")
Dad = Human(2, "Dad", "Da")
RandomPerson = Human(2, "Rando", "randoooo")



people = BinaryTree()

people.insert(Caleb)
people.insert(Grandpa)
people.insert(Yana)
people.insert(Baba)
people.insert(Mom)
people.insert(Dad)

people.insert(RandomPerson)


print("----------\nBefore:")
people.print_tree()

Grandpa.nickname = "Gramps" # Changing the name of Grandpa
people.replace(8, Grandpa)

print("----------\nAfter:")
people.print_tree()



# result = people.find(int(input("ID to find: ")))
# if result is not None:
#     print(f"---ID: {result.id} | NAME: {result.name} | NICKNAME: {result.nickname}")
# else:
#     print("Not found.")