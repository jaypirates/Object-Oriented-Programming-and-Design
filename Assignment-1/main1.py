A_List = CircularDoublyLinkedList()

while True:
    print('1.Add Node')
    print('2.Delete Node')
    print('3.Display ')
    print('4.Display  Sorting')
    print('5.Capacity ')
    print('6.List_capacity')
    print('7.Quit')

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
