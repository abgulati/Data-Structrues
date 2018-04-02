class StackNode:

	def __init__(self, data = None, nextNode = None):
		self.data = data
		self.nextNode = nextNode

	def setData(self, data):
		self.data = data

	def setNext(self, nextNode):
		self.nextNode = nextNode

	def getData(self):
		return self.data

	def getNext(self):
		return self.nextNode

class Stack:

	def __init__(self, top = None):
		self.top = None

	def isEmpty(self):
		if self.top is None:
			raise valueError("Cannot comply: stack is empty")

	def push(self, data):
		newNode = StackNode(data)
		newNode.nextNode = self.top
		self.top = newNode

	def pop(self):

		self.isEmpty()

		tempNode = self.top
		self.top = tempNode.getNext()
		data = tempNode.getData()
		tempNode.setData(None)
		tempNode.setNext(None)
		return data

	def size(self):

		self.isEmpty()

		tempNode = self.top
		count = 0

		while(tempNode):
			count = count + 1
			tempNode = tempNode.getNext()

		return count

	def search(self, data):

		self.isEmpty()

		tempNode = self.top

		while(tempNode):
			if (tempNode.getData() == data):
				print("Data is present")
				return
			tempNode = tempNode.getNext()

		print("Data not present in Stack")
		return

	def printStack(self):

		self.isEmpty()

		tempNode = self.top

		while(tempNode):
			print(tempNode.getData())
			tempNode = tempNode.getNext()

		return