from DLL import *

my_linked_list = Doubly_Linked_List()

def printer():
	print()
	print("List details are as follows:")
	print("The linked list currently holds the following data:")
	my_linked_list.printList()
	print()
	print("The size of this list is:", my_linked_list.size())
	print("List head is:",my_linked_list.getHead())
	print("List tail is:",my_linked_list.getTail())
	print()


max = input("Create doubly linked list from 0 to...? : ")
max = int(max)

for i in range(max, 0, -1):
	my_linked_list.insert(i)

printer()

x = input("Enter the data you're searching for: ")
x = int(x)

my_linked_list.search(x)

dlt = input("Enter the value you wish to delete: ")
dlt = int(dlt)

my_linked_list.delete(dlt)

printer()