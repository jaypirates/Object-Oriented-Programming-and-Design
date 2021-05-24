class CircularDoublyLinkedList:
    def __init__(self):
        self.first_node = None
        self.last_node = None
        self.pointer = 0
        self.list_capacity = []
        self.capacity = 2
        self.total_nodes = 0
        for i in range(self.capacity):
            empty_node = Node()
            self.list_capacity.append(empty_node)

    def insert(self):
        if self.first_node is None:

            added_node = Process()
            added_node.Add()
            self.list_capacity[self.pointer].add_values(added_node)
            self.first_node = self.list_capacity[self.pointer]
            self.pointer += 1
            self.last_node = self.first_node
            self.first_node.next = self.last_node
            self.first_node.prev = self.last_node
            self.last_node.next = self.first_node
            self.last_node.prev = self.first_node
            self.total_nodes = 1

        else:
            self.total_nodes += 1
            if self.total_nodes > self.capacity:
                increased_size_by = self.capacity
                self.capacity = self.capacity * 2
                for i in range(increased_size_by):
                    empty_node = Node()
                    self.list_capacity.append(empty_node)

            added_node = Process()
            added_node.Add()
            temp = self.last_node
            self.list_capacity[self.pointer].add_values(added_node)
            self.last_node.next = self.list_capacity[self.pointer]
            self.pointer += 1

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
            self.pointer = 0
            self.list_capacity.pop(0)
            extra_node = Node()
            self.list_capacity.append(extra_node)

            return
        else:
            self.total_nodes -= 1
            deleted_node = self.first_node
            self.last_node.next = self.first_node.next
            self.first_node = self.first_node.next
            self.first_node.prev = self.last_node
            deleted_node.data.display_all_attributes()
            self.pointer -= 1
            self.list_capacity.pop(0)
            extra_node = Node()
            self.list_capacity.append(extra_node)
            return

    def print_all(self):
        if self.first_node is None:
            print('List has no element')
        else:
            n = self.first_node
            print(n.data.display_all_attributes())
            n = n.next
            while n is not self.first_node:
                print(n.data.display_all_attributes())
                n = n.next

    def Sorting(self):
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
            if choice == 1:
                for i in range(len(List)):
                    for j in range(len(List) - 1):
                        if List[j].name > List[j + 1].name:
                            List[j], List[j + 1] = List[j + 1], List[j]
                for i in range(len(List)):
                    print(List[i].display_all_attributes())
            elif choice == 2:
                for i in range(len(List)):
                    for j in range(len(List) - 1):
                        if List[j].owner > List[j + 1].owner:
                            List[j], List[j + 1] = List[j + 1], List[j]
                for i in range(len(List)):
                    print(List[i].display_all_attributes())
            elif choice == 3:
                for i in range(len(List)):
                    for j in range(len(List) - 1):
                        if List[j].PID > List[j + 1].PID:
                            List[j], List[j + 1] = List[j + 1], List[j]
                for i in range(len(List)):
                    print(List[i].display_all_attributes())
            elif choice == 4:
                for i in range(len(List)):
                    for j in range(len(List) - 1):
                        if List[j].number_of_threads > List[j + 1].number_of_threads:
                            List[j], List[j + 1] = List[j + 1], List[j]
                for i in range(len(List)):
                    print(List[i].display_all_attributes())
            elif choice == 5:
                for i in range(len(List)):
                    for j in range(len(List) - 1):
                        if List[j].percent_of_cputime > List[j + 1].percent_of_cputime:
                            List[j], List[j + 1] = List[j + 1], List[j]
                for i in range(len(List)):
                    print(List[i].display_all_attributes())
            elif choice == 6:
                for i in range(len(List)):
                    for j in range(len(List) - 1):
                        if List[j].total_of_cputime > List[j + 1].total_of_cputime:
                            List[j], List[j + 1] = List[j + 1], List[j]
                for i in range(len(List)):
                    print(List[i].display_all_attributes())
            else:
                print("WRONG SELECTION")