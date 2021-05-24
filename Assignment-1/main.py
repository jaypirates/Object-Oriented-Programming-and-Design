'''import unittest

class testCircularDoublyLinkedList(unittest.TestCase):
    def testinsert(self):
  '''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.first_node = None
        self.last_node = None

        self.capacity = 2
        self.total_nodes = 0

    def insert(self):
        if self.first_node is None:

            added_node = Process()
            added_node.Add()
            self.first_node = Node(added_node)
            self.last_node = self.first_node
            self.first_node.next = self.last_node
            self.first_node.prev = self.last_node
            self.last_node.next = self.first_node
            self.last_node.prev = self.first_node
            self.total_nodes = 1

        else:
            self.total_nodes += 1
            if self.total_nodes > self.capacity:
                self.capacity = self.capacity*2

            added_node = Process()
            added_node.Add()
            temp = self.last_node
            self.last_node.next = Node(added_node)

            self.last_node = self.last_node.next
            self.last_node.prev = temp
            self.last_node.next = self.first_node
            self.first_node.prev = self.last_node


    def delete(self):
        if self.first_node is None:
            print('List is empty')
            return
        elif self.first_node == self.last_node:
            self.first_node.data.display_all_attributes()
            self.first_node = None
            self.last_node = None
            self.total_nodes = 0
            return
        else:
            self.total_nodes -= 1
            deleted_node = self.first_node
            self.last_node.next = self.first_node.next
            self.first_node = self.first_node.next
            self.first_node.prev = self.last_node
            deleted_node.data.display_all_attributes()
            return

    def print_all(self):
        if self.first_node is None:
            print('List has no element')
        else:
            n = self.first_node
            print(n.data.display_all_attributes())
            n=n.next
            while n is not self.first_node:
                print(n.data.display_all_attributes())
                n = n.next

    def Sorting(self):
        if self.first_node == None :
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
            if choice == 1:
                for i in range(len(List)):
                    for j in range(len(List) - 1):
                        if List[j].name.lower() > List[j + 1].name.lower():
                            List[j],List[j+1] = List[j+1], List[j]
                for i in range(len(List)):
                    print(List[i].display_all_attributes())
            elif choice == 2:
                for i in range(len(List)):
                    for j in range(len(List) - 1):
                        if List[j].owner.lower() > List[j + 1].owner.lower():
                            List[j],List[j+1] = List[j+1], List[j]
                for i in range(len(List)):
                    print(List[i].display_all_attributes())
            elif choice == 3:
                for i in range(len(List)):
                    for j in range(len(List) - 1):
                        if List[j].PID > List[j + 1].PID:
                            List[j],List[j+1] = List[j+1], List[j]
                for i in range(len(List)):
                    print(List[i].display_all_attributes())
            elif choice == 4:
                for i in range(len(List)):
                    for j in range(len(List) - 1):
                        if List[j].number_of_threads > List[j + 1].number_of_threads:
                            List[j],List[j+1] = List[j+1], List[j]
                for i in range(len(List)):
                    print(List[i].display_all_attributes())
            elif choice == 5:
                for i in range(len(List)):
                    for j in range(len(List) - 1):
                        if List[j].percent_of_cputime > List[j + 1].percent_of_cputime:
                            List[j],List[j+1] = List[j+1], List[j]
                for i in range(len(List)):
                    print(List[i].display_all_attributes())
            elif choice == 6:
                for i in range(len(List)):
                    for j in range(len(List) - 1):
                        if List[j].total_of_cputime > List[j + 1].total_of_cputime:
                            List[j],List[j+1] = List[j+1], List[j]
                for i in range(len(List)):
                    print(List[i].display_all_attributes())
            else:
                print("WRONG SELECTION")


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
        print("Name of Process : "+self.name)
        print("Name of Owner : " + self.owner)
        print("PID : " + self.PID)
        print("Number of Threads : " + self.number_of_threads)
        print("Percent of CPU time : " + self.percent_of_cputime)
        print("Total time of CPU : " + self.total_of_cputime)




A_List = CircularDoublyLinkedList()

while True:
    print('1.Add Node')
    print('2.Delete Node')
    print('3.Display')
    print('4.Sorting')
    print('5.Capacity')
    print('6.Quit')

    do = int(input('What would you like to do'))
    if do == 1:
        A_List.insert()
    elif do == 2:
        A_List.delete()
    elif do == 3:
        A_List.print_all()
    elif do == 4:
        A_List.Sorting()
    elif do == 5:
        print("Capacity")
        print(A_List.capacity)
        print("Total number of Nodes")
        print(A_List.total_nodes)
    elif do == 6:
        print("Thanks for using Linked List")
        break
    else:
        print("WRONG SELECTION")
        break


