class Node:

	def __init__(self, data = None, prevNode = None, nextNode = None):
		self.data = data
		self.prevNode = prevNode
		self.nextNode = nextNode

	def setData(self, data):
		self.data = data

	def setNext(self, nextNode):
		self.nextNode = nextNode

	def setPrev(self, prevNode):
		self.prevNode = prevNode

	def getData(self):
		return self.data

	def getNext(self):
		return self.nextNode

	def getPrev(self):
		return self.prevNode

class Doubly_Linked_List:

	def __init__(self, head = None, tail = None):
		self.head = head
		self.tail = tail

	def insert(self, data):
		newNode = Node(data)
		newNode.setPrev(None)
		
		if self.head is None:			#i.e. the list is empty, so set next as none, and initialize this node as the head and tail
			newNode.setNext(None)
			self.head = newNode
			self.tail = newNode
		else:
			tempNode = self.head
			tempNode.setPrev(newNode)
			newNode.setNext(tempNode)
			self.head = newNode

	def emptyTest(self):
		if self.head is None:
			raise Exception("Cannot comply: list is empty!")

	def getHead(self):
		self.emptyTest()
		return self.head.getData()

	def getTail(self):
		self.emptyTest()
		return self.tail.getData()

	def printList(self):

		self.emptyTest()

		currentNode = self.head

		while(currentNode):
			print(currentNode.getData())
			currentNode = currentNode.getNext()

	def size(self):

		self.emptyTest()

		currentNode = self.head
		count = 0

		while(currentNode):
			count = count + 1
			currentNode = currentNode.getNext()

		return count

	def search(self, value):

		self.emptyTest()

		currentNode = self.head

		while(currentNode):
			if(currentNode.getData() == value):
				print("Data is present in the list!")
				print("Data linkage is as follows:")

				if currentNode.getPrev() is not None:						#i.e. if current node is not the head
					print("Prev data:", currentNode.getPrev().getData())
				else:
					print("This is the head node, no previous data")

				if currentNode.getNext() is not None:						#i.e. if current not is not the tail
					print("Next data:", currentNode.getNext().getData())
				else:
					print("This is the tail node, no next data")

				return
			currentNode = currentNode.getNext()

		print("Sorry, data not present in the list")
		return

	def delete(self, data):

		self.emptyTest()

		currentNode = self.head

		if (currentNode.getData() == data):			#testing to see if the head node is to be deleted
			if currentNode.getNext():				#testing to see if the list is not just the head node, equivalent to if self.size() is not 1
				self.head = currentNode.getNext()
				currentNode.getNext().setPrev(None)
				currentNode.setNext(None)
				currentNode.setData(None)
			else:
				currentNode.setData(None)
				self.head = None 					#i.e. now the list will be empty, since it was just the head node anyways, the next & prev attributes were already None
				self.tail = None
				print("The value has been deleted, the list is now empty")
			return

		if not currentNode.getNext():				#i.e. the list comprises of only the head node and that head node does not hold the data to be deleted
			print("That value is not in the list!")
			return

		currentNode = currentNode.getNext()
		
		while(currentNode):
			if not currentNode.getNext():			#The current node is the tail node, so no next node
				if currentNode.getData() == data:
					self.tail = currentNode.getPrev()
					currentNode.getPrev().setNext(None)
					currentNode.setData(None)
					currentNode.setPrev(None)
					return

			if (currentNode.getData() == data):
				currentNode.getPrev().setNext(currentNode.getNext())
				currentNode.getNext().setPrev(currentNode.getPrev())
				currentNode.setData(None)
				currentNode.setPrev(None)
				currentNode.setNext(None)
				print("Value deleted")
				return
			currentNode = currentNode.getNext()

		print("Sorry, value not in list, cannot delete")
		return