from SLL import *

my_linked_list = SinglyLinkedList()

my_linked_list.insert(5)
my_linked_list.insert(4)
my_linked_list.insert(3)
my_linked_list.insert(2)
my_linked_list.insert(1)

print("Size of the current linked list is: ", my_linked_list.size())
my_linked_list.printList()

x = input("Insert the value you're searching for: ")
my_linked_list.search(int(x))

y = input("Enter the value you want to delete from the list: ")
my_linked_list.deleteNode(int(y))
my_linked_list.printList()