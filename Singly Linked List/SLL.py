class ListNode(object):

	def __init__(self, data = None, nextNode = None):
		self.data = data
		self.next = nextNode

	def getData(self):
		return self.data

	def getNext(self):
		return self.nextNode

	def setData(self, x):
		self.data = x

	def setNext(self, newNext):
		self.nextNode = newNext

class SinglyLinkedList(object):

	def __init__(self, head = None):
		self.head = head

	def insert(self, data):
		newNode = ListNode(data)
		newNode.setNext(self.head)
		self.head = newNode

	def printList(self):

		currentNode = self.head

		if (self.head == None):
			raise Exception("Empty List")

		while (currentNode):
			print(currentNode.getData())
			currentNode = currentNode.getNext()

	def searchList(self, data):

		currentNode = self.head

		if (self.head == None):
			raise Exception("Empty List")

		found = False
		while(currentNode and (found is False)):
			if (currentNode.getData() == data):
				found = True
			else:
				currentNode = currentNode.getNext()

		if (found is True):
			print("Value present!")
			return currentNode
		else:
			print("The value is not present in this linked list")
			#raise ValueError("Value not present in list")

	def size(self):
		currentNode = self.head

		if (self.head == None):
			raise Exception("List is empty!")

		count = 0
		while(currentNode):
			count = count + 1
			currentNode = currentNode.getNext()

		return count


my_linked_list = SinglyLinkedList()

my_linked_list.insert(3)
my_linked_list.insert(2)
my_linked_list.insert(1)

my_linked_list.printList()

listSize = my_linked_list.size()
print("Size of the list is:", listSize)

x = input("Enter the data you're searching for: ")
resultNode = my_linked_list.searchList(int(x))
