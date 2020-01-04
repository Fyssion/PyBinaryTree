if __name__ == "__main__":

    from bintree import BinaryTree


    # Creating a Human class to store data.
    # Remember to include an ID variable when creating your own class.
    class Human:
        """A human with attributes of id, name, and nickname."""
        def __init__(self, id, name):
            self.id = id
            self.name = name
            self.nickname = None

    class Data:
        def __init__(self, id):
            self.id = id


    list_of_IDs = [5, 8, 4, 6, 11, 2, 7, 9, 25, 14, 3, 1, 36, 51, 52]

    # Human(id, name, nickname)
    # Creating example people to store
    Clam = Human(5, "Clam")
    Nator = Human(8, "Nator")
    Robot = Human(4, "Robot")
    Nate = Human(6, "Nate")
    Dave = Human(11, "Dave")
    Joe = Human(2, "Joe")
    Jake = Human(7, "Jake")


    # Creating and initiating the BinaryTree
    people = BinaryTree()

    for ID in list_of_IDs:
        people.insert(Data(ID))

    # Inserting people into the tree with insert()
    # people.insert(Clam)
    # people.insert(Nator)
    # people.insert(Robot)
    # people.insert(Nate)
    # people.insert(Dave)
    # people.insert(Joe)
    # people.insert(Jake)


    # Printing the tree before and after replacing the data of a node
    # print("----------\nBefore:")
    # people.print_tree()

    # Nator.nickname = "Robo.Nator" # Changing the name of Nator
    # people.replace(8, Nator)

    # print("----------\nAfter:")
    # people.print_tree()

    # Printing the length of a tree
    print(f"---------\nLength: {people.length()}")

    # Finding the distance to the farthest node
    distance, data = people.dist_to_farthest()
    print(f"Distance to farthest node: {distance} | Corresponding ID: {data.id}")

    people.display()


    # Finding a node in the tree by ID
    # result = people.find(int(input("ID to find: ")))
    # if result is not None:
    #     print(f"---ID: {result.id} | NAME: {result.name} | NICKNAME: {result.nickname}")
    # else:
    #     print("Not found.")