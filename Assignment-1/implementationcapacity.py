import unittest

# Node class for maintaining the structure of Linked List

class Node:
    def __init__(self):
        self.data = None
        self.next = None
        self.prev = None

    def add_values(self, data):
        self.data = data
        self.next = None
        self.prev = None

# implementing the process nodes and adding,deleting, displaying and sorting nodes
# empty nodes of Node class are created with capacity 2
# the capacity of node is checked when any node is added to queue
# and if needed capacity is to be doubled by comparing capacity with total nodes in list

class CircularDoublyLinkedList:
    def __init__(self):
        self.first_node = None
        self.last_node = None
        self.pointer_to_current_node = 0
        self.list_capacity = []
        self.capacity = 2
        self.total_nodes = 0
        for i in range(self.capacity):
            empty_node = Node()
            self.list_capacity.append(empty_node)

    # insert method help to insert nodes in Linked List
    # It calls add_values function from Node class which sets the Process values to node
    # pointer_to_current_node points to last initiated node
    # so by use of pointer_to_current_node we can differetiate between null and used nodes

    def insert(self):
        # if condition will run only for 1 time when first node is inserted
        # here the head_node and tail_node are initiated

        if self.first_node is None:
            adding_values_to_node = Process()
            adding_values_to_node.Add()
            self.list_capacity[self.pointer_to_current_node].add_values(adding_values_to_node)
            self.first_node = self.list_capacity[self.pointer_to_current_node]
            self.pointer_to_current_node += 1
            self.last_node = self.first_node
            self.first_node.next = self.last_node
            self.first_node.prev = self.last_node
            self.last_node.next = self.first_node
            self.last_node.prev = self.first_node
            self.total_nodes = 1

        # else will run for adding all nodes to List except for first one
        # nodes are added just by using tail_node and head_node
        # list_capacity contains all the nodes, null nodes and initialized nodes

        else:
            self.total_nodes += 1
            if self.total_nodes > self.capacity:
                increased_size_by = self.capacity
                self.capacity = self.capacity * 2
                for i in range(increased_size_by):
                    empty_node = Node()
                    self.list_capacity.append(empty_node)
            adding_values_to_node = Process()
            adding_values_to_node.Add()
            temp = self.last_node
            self.list_capacity[self.pointer_to_current_node].add_values(adding_values_to_node)
            self.last_node.next = self.list_capacity[self.pointer_to_current_node]
            self.pointer_to_current_node += 1
            self.last_node = self.last_node.next
            self.last_node.prev = temp
            self.last_node.next = self.first_node
            self.first_node.prev = self.last_node

    # delete function works by poping the first element from list_capacity
    # And by changing the next and prev pointers of head node and last node

    def delete(self):
        # if condition will check if List is empty or not
        if self.first_node is None:
            print('List is empty')
            return

        # elif will run when deleting the last node, by exchanging the address of nodes
        elif self.first_node == self.last_node:
            self.first_node.data.display_all_attributes()
            self.first_node = None
            self.last_node = None
            self.total_nodes = 0
            self.pointer_to_current_node = 0
            self.list_capacity.pop(0)
            extra_node = Node()
            self.list_capacity.append(extra_node)
            return

        # else will run for deleting all nodes one at a time, except for the last one
        else:
            self.total_nodes -= 1
            deleted_node = self.first_node
            self.last_node.next = self.first_node.next
            self.first_node = self.first_node.next
            self.first_node.prev = self.last_node
            deleted_node.data.display_all_attributes()
            self.pointer_to_current_node -= 1
            self.list_capacity.pop(0)
            extra_node = Node()
            self.list_capacity.append(extra_node)
            return

    # print_all method is used for displaying all Values of all nodes using while loop
    # it used display_all_attributes method defined in Process Class to print node values

    def print_all(self):
        # if will run when List is empty
        if self.first_node is None:
            print('List has no element')

        # else will run when at least one node is in List to display
        else:
            n = self.first_node
            print(n.data.display_all_attributes())
            n = n.next
            while n is not self.first_node:
                print(n.data.display_all_attributes())
                n = n.next

    # sorting method is used for displaying all nodes in particular sorting order
    def sorting(self):
        # if condition checks if there are nodes to display or not by checking head node
        if self.first_node == None:
            print("LIST HAS NO ELEMENTS TO SORT OR DISPLAY")
        else:
            List = []
            current_node = self.first_node
            List.append(current_node.data)
            current_node = current_node.next
            while current_node is not self.first_node:
                List.append(current_node.data)
                current_node = current_node.next

            print("SORT BY : ")
            print("1.Name")
            print("2.Owner")
            print("3.PID")
            print("4.Number of Threads")
            print("5.Percent of CPU Time")
            print("6.Total of CPU Time")
            choice = int(input())

            # Sorting is done by using the pointer to current node and its next node
            # choice=1 for sorting all Nodes with Name Variable using Bubble Sort
            if choice == 1:
                for i in range(len(List)):
                    for j in range(len(List) - 1):
                        if List[j].name > List[j + 1].name:
                            List[j], List[j + 1] = List[j + 1], List[j]
                for i in range(len(List)):
                    print(List[i].display_all_attributes())

            # choice=2 for sorting all Nodes with Owner of Process using bubble sort
            elif choice == 2:
                for i in range(len(List)):
                    for j in range(len(List) - 1):
                        if List[j].owner > List[j + 1].owner:
                            List[j], List[j + 1] = List[j + 1], List[j]
                for i in range(len(List)):
                    print(List[i].display_all_attributes())

            # choice=3 for sorting all Nodes with PID using Bubble Sort
            elif choice == 3:
                for i in range(len(List)):
                    for j in range(len(List) - 1):
                        if List[j].PID > List[j + 1].PID:
                            List[j], List[j + 1] = List[j + 1], List[j]
                for i in range(len(List)):
                    print(List[i].display_all_attributes())

            # choice=4 for sorting all Nodes with number of Threads using Bubble Sort
            elif choice == 4:
                for i in range(len(List)):
                    for j in range(len(List) - 1):
                        if List[j].number_of_threads > List[j + 1].number_of_threads:
                            List[j], List[j + 1] = List[j + 1], List[j]
                for i in range(len(List)):
                    print(List[i].display_all_attributes())

            # choice=5 for sorting all Nodes with Percent of Cputime used by process
            elif choice == 5:
                for i in range(len(List)):
                    for j in range(len(List) - 1):
                        if List[j].percent_of_cputime > List[j + 1].percent_of_cputime:
                            List[j], List[j + 1] = List[j + 1], List[j]
                for i in range(len(List)):
                    print(List[i].display_all_attributes())

            # choice=6 for sorting all nodes with total of Cputime used by process
            elif choice == 6:
                for i in range(len(List)):
                    for j in range(len(List) - 1):
                        if List[j].total_of_cputime > List[j + 1].total_of_cputime:
                            List[j], List[j + 1] = List[j + 1], List[j]
                for i in range(len(List)):
                    print(List[i].display_all_attributes())

            # else will run whenever user enter anything except 1-6
            else:
                print("WRONG SELECTION")


# Process class contains the all elements of Nodes and function to display all the elements
# add() function takes the data from user to set the values of process in nodes
# display_all_attributes() outputs the value of process of particular node

class Process:
    def __init__(self):
        self.name = None
        self.owner = None
        self.PID = None
        self.number_of_threads = None
        self.percent_of_cputime = None
        self.total_of_cputime = None

    def Add(self):
        self.name = input("Name of Process : ")
        self.owner = input("Name of Owner : ")
        self.PID = input("PID : ")
        self.number_of_threads = input("Number of Threads : ")
        self.percent_of_cputime = input("Percent of CPU time : ")
        self.total_of_cputime = input("Total time of CPU : ")

    def display_all_attributes(self):
        print("Name of Process : " + self.name)
        print("Name of Owner : " + self.owner)
        print("PID : " + self.PID)
        print("Number of Threads : " + self.number_of_threads)
        print("Percent of CPU time : " + self.percent_of_cputime)
        print("Total time of CPU : " + self.total_of_cputime)

#ASSIGNMENT-1
#RedID - 824672518
#Name - Patel Jay Prabhubhai
#version-1.0


# main Program

A_List = CircularDoublyLinkedList()

# while loop for running and working with List
# it takes the user input and calls the function accordingly
# all the functions are implemented in class CircularDoublyLinkedList()

while True:
    print('1.Add Node')
    print('2.Delete Node')
    print('3.Display ')
    print('4.Display  Sorting')
    print('5.Capacity ')
    print('6.List_capacity')
    print('7.Quit')

    do = int(input('What would you like to do'))

    # if else will run as per user input for working with List
    if do == 1:
        A_List.insert()
    elif do == 2:
        A_List.delete()
    elif do == 3:
        A_List.print_all()
    elif do == 4:
        A_List.sorting()
    elif do == 5:
        print("Total number of Nodes")
        print(A_List.total_nodes)
        print("Original Length")
        print(len(A_List.list_capacity))
    elif do == 6:
        for i in range(A_List.total_nodes):
            print(A_List.list_capacity[i].data.display_all_attributes())
    elif do == 7:
        print("Thanks for using Linked List")
        break
    else:
        print("WRONG SELECTION")
        break


class TestLinkedList(unittest.TestCase):
    def test_sorting(self):
        sorting = [3,5,6,2,1,4]
        for i in range(len(sorting)):
            for j in range(len(sorting)-1):
                if sorting[j] > sorting[j+1]:
                    sorting[j],sorting[j+1] = sorting[j+1],sorting[j]
        sorted = [1,2,3,4,5,6]
        self.assertEqual(sorting,sorting)



if __name__ == '__main__':
    unittest.main()