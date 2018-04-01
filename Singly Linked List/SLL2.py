class Node(object):

	def __init__(self, data = None, nextNode = None):
		self.data = data
		self.nextNode = nextNode

	def getData(self):
		return self.data

	def getNext(self):
		return self.nextNode

	def setData(self, data):
		self.data = data

	def setNext(self, newNode):
		self.nextNode = newNode

class SinglyLinkedList(object):

	def __init__(self, head = None):
		self.head = head

	def insert(self, data):
		newNode = Node(data)
		newNode.setNext(self.head)
		self.head = newNode

	def emptyTest(self):
		if(self.head == None):
			raise Exception("Cannot complete opearion: the list is empty.")

	def size(self):

		self.emptyTest()

		currentNode = self.head
		count = 0

		while(currentNode):
			count = count + 1
			currentNode = currentNode.getNext()

		return count

	def printList(self):

		self.emptyTest()

		currentNode = self.head

		while(currentNode):
			print(currentNode.getData())
			currentNode = currentNode.getNext()

	def search(self, value):

		self.emptyTest()

		currentNode = self.head

		while(currentNode):
			if(currentNode.getData() == value):
				print("The value is present in the list!")
				return
			currentNode = currentNode.getNext()

		print("The value is not present in the given list")

	def deleteNode(self, value):

		self.emptyTest()

		currentNode = self.head
		if(currentNode.getData() == value):
			self.head = currentNode.getNext()
			currentNode.setData(None)
			currentNode.setNext(None)
			return

		currentNode = currentNode.getNext()

		while(currentNode):
			if(currentNode.getNext().getData() == value):
				tempNode = currentNode.getNext()
				currentNode.setNext(tempNode.getNext())
				tempNode.setData(None)
				tempNode.setNext(None)

				return

			currentNode = currentNode.getNext()

		raise valueError("That value is not present in the list")