import SLL

my_linked_list = SinglyLinkedList()

my_linked_list.insert(3)
my_linked_list.insert(2)
my_linked_list.insert(1)

my_linked_list.printList()

listSize = my_linked_list.size()
print("Size of the list is:", listSize)

x = input("Enter the data you're searching for: ")
resultNode = my_linked_list.searchList(int(x))